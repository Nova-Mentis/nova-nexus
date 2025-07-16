import anvil.secrets
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import random

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
def get_tenants():
  tenant_list = []
  for row in app_tables.tenants.search():
    tenant_list.append((row["tenant_name"], row))
  return tenant_list

@anvil.server.callable
def generate_tenant_id(tenant_name):
  base_id = tenant_name.lower().replace(' ', '')
  suffix = str(random.randint(100, 999))  # 3-digit random number
  tenant_id = f"{base_id}_{suffix}"
  return tenant_id

@anvil.server.callable
def get_assigned_tenant(user):
  return user['asssigned_tenant']
  
