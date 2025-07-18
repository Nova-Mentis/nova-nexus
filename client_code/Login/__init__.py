from ._anvil_designer import LoginTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Login(LoginTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def login_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.users.login_with_form()
    print("[Login] Current User is " + anvil.users.get_user()['email'])
    print("[Login] Permissions are: " + anvil.users.get_user()['role']['role_name'])
    anvil.server.call('set_up_cookies')
    open_form('DashboardPage')
    pass
