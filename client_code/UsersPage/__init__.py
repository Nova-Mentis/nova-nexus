from ._anvil_designer import UsersPageTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import State

class UsersPage(UsersPageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.user_list_panel.items = anvil.server.call('get_users_by_tenant', tenant=State.tenant)
    self.user_list_panel.add_event_handler('x-edit-user', self.handle_edit_user)
    # Any code you write here will run before the form opens.

  def handle_edit_user(self, user, **event_args):
    pass
