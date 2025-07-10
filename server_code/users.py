import anvil.secrets
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from .exceptions import UpdateUserFailedError

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
def update_user_profile(first_name, last_name, email):
  try:
    user = app_tables.users.get(email=email)
    user.update(first_name=first_name, last_name=last_name)
    print("Successfully updated " + email)
    return True
  except UpdateUserFailedError:
    print("Failed to update user " + email)
    return False

@anvil.server.callable
def get_users_by_tenant(tenant):
  user_list = app_tables.users.search(assigned_tenant=tenant)
  return user_list
    
  
