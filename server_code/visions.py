import anvil.secrets
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime

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
def get_vision_types():
  vision_type_list = []
  for row in app_tables.vision_types.search():
    vision_type_list.append((row["vision_type_name"], row))
  return vision_type_list

@anvil.server.callable
def get_vision_components():
  vision_components_list = []
  for row in app_tables.vision_components.search():
    vision_components_list.append((row["vision_component"], row))
  return vision_components_list

@anvil.server.callable
def get_visions_list(user, tenant):
  return app_tables.visions.search(
    tables.order_by("created_at", ascending=False), 
    user=user, 
    tenant=tenant
  )

@anvil.server.callable
def count_visions(user, tenant):
  vision_list = app_tables.visions.search(
    user=user, 
    tenant=tenant
  )
  return len(vision_list)

@anvil.server.callable
def create_vision(vision_name, vision_statement, user, vision_type, tenant):
  print("Adding " + vision_name + " vision")
  current_datetime = datetime.now()
  app_tables.visions.add_row(vision_name=vision_name, vision_statement=vision_statement, user=user, vision_type=vision_type, created_at=current_datetime, tenant=tenant)
  created_vision = app_tables.visions.search(vision_name=vision_name)
  return created_vision

@anvil.server.callable
def delete_vision(vision):
  # check that the vision being deleted exists in the Data Table
  if app_tables.visions.has_row(vision):
    
    # First clean up vision steps, step questions, question response options and user scores
    # Question Scores
    anvil.server.call('delete_score', vision=vision)

    # Step Scores
    for user_step_score_row in app_tables.user_step_scores.search(vision=vision):
      user_step_score_row.delete()

    # Step Questions
    for step_questions_row in app_tables.step_questions.search(vision=vision):
      # Step Question Response Options
      for step_question_response_type_row in app_tables.step_question_response_options.search(question=step_questions_row):
        step_question_response_type_row.delete()
      step_questions_row.delete() 

    # Steps
    for steps_row in app_tables.steps.search(vision=vision):
      steps_row.delete() 
      
    # Finally remove vision
    vision.delete()
  else:
    raise Exception("Vision does not exist")

@anvil.server.callable
def get_questions_for_vision_type(vision_type):
  questions_list = app_tables.vision_guide_questions.search(vision_type=vision_type)
  return questions_list
