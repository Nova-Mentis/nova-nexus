import anvil.secrets
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

# Called at login
@anvil.server.callable 
def set_up_cookies():
  print("Setting up cookies")
  anvil.server.cookies.local['tenant'] = anvil.server.call('get_assigned_tenant', anvil.users.get_user())

# Called to setup tenant
@anvil.server.callable
def get_cookies_tenant():
  return anvil.server.cookies.local['tenant']

@anvil.server.callable
def switch_cookies_tenant(tenant):
  print("Switching tenant to " + tenant['tenant_name'])
  anvil.server.cookies.local['tenant'] = tenant