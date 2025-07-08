from ._anvil_designer import HomePageTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class HomePage(HomePageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    anvil.users.login_with_form()

    # Any code you write here will run before the form opens.

  def clear_content_panel(self):
    self.content_panel.clear()
    self.content_panel.add_component()

  def visions_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Visions')
    pass

  def dashboard_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Dashboard')
    pass

  def logout_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.users.logout()
    pass
