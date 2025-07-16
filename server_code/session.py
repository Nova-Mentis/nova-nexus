import anvil.secrets
import anvil.users
import anvil.server

# Called at login
@anvil.server.callable 
def set_up_session():
  # Session ID already available on anvil.server.get_session_id
  # Current User already available on anvil.users.get_user()
  anvil.server.session['tenant'] = anvil.server.call('get_assigned_tenant', anvil.users.get_user())

# Called to setup tenant
@anvil.server.callable
def get_session_tenant():
  return anvil.server.session['tenant']

@anvil.server.callable
def switch_session_tenant(tenant):
  print("Switching tenant to " + tenant['tenant_name'])
  anvil.server.session['tenant'] = tenant