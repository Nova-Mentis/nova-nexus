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
def update_user_profile(first_name, last_name, email, role, tenant):
  print("Updating user " + email)
  try:
    print("Getting user object from DB")
    user = get_user_by_email(email)

    # Check role change
    if user['role']['role_name'] != role['role_name']:
      print("Old role is " + user['role']['role_name'] + " new role will be " + role['role_name'])
      new_role = app_tables.user_role_types.search(role_name=role)
      user.update(role=new_role)
      print("Updated user role to" + new_role['role_name'])

    # Check tenant change
    if user['assigned_tenant']['tenant_name'] != tenant['tenant_name']:
      new_tenant = app_tables.tenants.search(tenant_name=tenant['tenant_name'])
      user.update(assigned_tenant=new_tenant)
      print("Updated user tenant to" + new_tenant['tenant_name'])
    
    user.update(first_name=first_name, last_name=last_name, email=email)
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

@anvil.server.callable
def get_user_roles():
  user_roles = []
  for row in app_tables.user_role_types.search():
    user_roles.append((row["role_name"], row))
  return user_roles

@anvil.server.callable
def get_user_by_email(email):
  user = app_tables.users.get(email=email)
  return user
    
  
