import anvil.secrets
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from . import time
from . import tools
from . import visions
from . import scores
# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#

@anvil.server.callable
def get_steps_list(vision):
  return app_tables.steps.search(
    tables.order_by("created_at", ascending=False), 
    vision=vision
  )

@anvil.server.callable
def add_new_step(step_name, step_description, vision, ai_generated=False):
  print("Adding " + step_name + " step to " + vision['vision_name'])
  current_datetime = time.get_utc_time()
  step_id = tools.generate_hash_id(seed=step_name)
  app_tables.steps.add_row(step_name=step_name, 
                           step_description=step_description, 
                           created_at=current_datetime, 
                           vision=vision, 
                           ai_generated=ai_generated,
                           step_id=step_id
                          )
  # Update Vision
  step = app_tables.steps.get(step_id=step_id)
  visions.add_step_to_vision(step=step, vision=vision)

@anvil.server.callable
def remove_step(step):
  # check that the step being deleted exists in the Data Table
  if app_tables.steps.has_row(step):
    # First clean up step questions, question response options and user scores
    # Question Scores
    scores.delete_score(step=step)

    # Step Scores
    for user_step_score_row in app_tables.step_scores.search(step=step):
      user_step_score_row.delete()

    # Step Questions
    for step_questions_row in app_tables.step_questions.search(step=step):
      step_questions_row.delete()

    # Remove step from Vision
    vision = step['vision']
    if vision and app_tables.visions.has_row(vision):
      if step in vision['steps']:
        vision['steps'].remove(step)
        vision.update(steps=vision['steps'])

    # Finally remove step
    step.delete()
  else:
    raise Exception("Step does not exist")

@anvil.server.callable
def update_step(step_id, **updates):
  """
  Updates a step row dynamically based on a dictionary of field:value pairs.
  `step_id`: ID of the step to update.
  `updates`: Dictionary with keys matching the step table column names.
  """
  print(f"[update_step] Updating step: {step_id}")

  # Get the step row
  step_row = app_tables.steps.get(step_id=step_id)
  if not step_row:
    print("[update_step] step not found.")
    return False

  # Get list of valid column names
  valid_columns = [col['name'] for col in app_tables.steps.list_columns()]

  for key, value in updates.items():
    if key in valid_columns:
      try:
        step_row[key] = value  # ✅ This is correct if key is a string
      except Exception as e:
        print(f"[update_step] Failed to update '{key}': {e}")
    else:
      print(f"[update_step] Warning: Column '{key}' does not exist on the step table and was skipped.")

  return step_row
