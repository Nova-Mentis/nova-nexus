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
def update_user_profile(email, updates):
  """
  Updates a user's profile using partial updates via a dictionary.
  Example `updates`: {
      "first_name": "John",
      "last_name": "Doe",
      "role": {"role_name": "admin"},
      "tenant": {"tenant_name": "Acme Corp"}
  }
  """
  print(f"Updating user: {email}")
  try:
    user = get_user_by_email(email)
    if not user:
      print("User not found.")
      return False

    fields_to_update = {}

    # Update name/email fields if present
    for field in ['first_name', 'last_name', 'email']:
      if field in updates and updates[field] != user[field]:
        fields_to_update[field] = updates[field]
        print(f"Updating {field} to {updates[field]}")

    # Handle role update
    if 'role' in updates and updates['role']:
      new_role_name = updates['role'].get('role_name')
      if user['role']['role_name'] != new_role_name:
        new_role = app_tables.user_role_types.get(role_name=new_role_name)
        if new_role:
          fields_to_update['role'] = new_role
          print(f"Updating role to {new_role_name}")
        else:
          print(f"Role '{new_role_name}' not found in DB")

    # Handle tenant update
    if 'tenant' in updates and updates['tenant']:
      new_tenant_name = updates['tenant'].get('tenant_name')
      if user['assigned_tenant']['tenant_name'] != new_tenant_name:
        new_tenant = app_tables.tenants.get(tenant_name=new_tenant_name)
        if new_tenant:
          fields_to_update['assigned_tenant'] = new_tenant
          print(f"Updating tenant to {new_tenant_name}")
        else:
          print(f"Tenant '{new_tenant_name}' not found in DB")

    if fields_to_update:
      user.update(**fields_to_update)
      print("User profile updated successfully.")
    else:
      print("No updates were necessary.")

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
    
  
