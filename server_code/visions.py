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
  vision_list = app_tables.visions.search(user=user, tenant=tenant)
  return vision_list


@anvil.server.callable
def create_vision(vision_name, vision_statement, user, vision_type, tenant):
  print("Adding " + vision_name + " vision")
  current_datetime = datetime.now()
  app_tables.visions.add_row(vision_name=vision_name, vision_statement=vision_statement, user=user, vision_type=vision_type, created_at=current_datetime, tenant=tenant)
  created_vision = app_tables.visions.search(vision_name=vision_name)
  return created_vision

#@anvil.server.callable
#def delete_vision(vision):

@anvil.server.callable
def get_questions_for_vision_type(vision_type):
  questions_list = app_tables.vision_guide_questions.search(vision_type=vision_type)
  return questions_list
