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
  except Exception as e:
    print("An unexpected error occurred:", e)
    return False

@anvil.server.callable
def get_users_by_tenant(tenant):
  user_list = app_tables.users.search(assigned_tenant=tenant)
  return user_list

@anvil.server.callable(require_user=True)
def change_email(email):
  user = anvil.users.get_user()
  try:
    user["email"] = email
    print("Customer email updated successfully")
  except Exception as e:
    print("An error occurred when updating a user's email:", e)
  return user

@anvil.server.callable(require_user=True)
def delete_user():
  user = anvil.users.get_user()
  if user["stripe_id"]:
    try: 
      user.delete()
    except Exception as e:
      print("An unexpected error occurred:", e)

@anvil.server.callable
def verify_subscription(user):
  if user['subscription']:
    return True
  else:
    return False
    
  
