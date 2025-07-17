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
    for user_step_score_row in app_tables.user_step_scores.search(step=step):
      user_step_score_row.delete()

    # Step Questions
    for step_questions_row in app_tables.step_questions.search(step=step):
      # Step Question Response Options
      for step_question_response_type_row in app_tables.step_question_response_options.search(question=step_questions_row):
        step_question_response_type_row.delete()
      step_questions_row.delete() 

    # Finally remove step
    step.delete()
  else:
    raise Exception("Step does not exist")
