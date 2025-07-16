import anvil.server

# Session ID already available on anvil.server.get_session_id
# Current User already available on anvil.users.get_user()

@anvil.server.callable
def get_session_id():
  return anvil.server.get_session_id()