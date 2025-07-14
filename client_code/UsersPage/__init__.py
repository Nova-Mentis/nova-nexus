from ._anvil_designer import UsersPageTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import State
from .EditUserForm import EditUserForm
from .AddUserForm import AddUserForm

class UsersPage(UsersPageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.refresh_user_list()
    self.user_list_panel.add_event_handler('x-edit-user', self.handle_edit_user)
    self.user_list_panel.add_event_handler('x-refresh-user-list', self.handle_refresh_user_list)
    # Any code you write here will run before the form opens.

  def handle_edit_user(self, user, **event_args):
    alert(
      content=EditUserForm(user=user),
      large=True,
      buttons=""
    )
    pass

  def refresh_user_list(self):
    self.user_list_panel.items = anvil.server.call('get_users_by_tenant', tenant=State.tenant)

  def handle_refresh_user_list(self):
    self.refresh_user_list()

  def add_user_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    alert(
      content=AddUserForm(),
      large=True,
      buttons=""
    )
    pass
