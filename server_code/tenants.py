import anvil.secrets
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from . import tools

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
  tenant_id = tools.generate_hash_id(seed=tenant_name)
  return tenant_id

@anvil.server.callable
def get_assigned_tenant(user):
  return user['assigned_tenant']
  
