from ._anvil_designer import HomePageTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import State
from ..VisionsPage import VisionsPage
from ..DashboardPage import DashboardPage

class HomePage(HomePageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.logged_in_text.text = "Logged in as " + anvil.users.get_user()['email']
    self.content_panel.clear()
    self.content_panel.add_component(DashboardPage())

    # Any code you write here will run before the form opens.

  def logout_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.users.logout()
    open_form('Login')
    pass

  def dashboard_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.content_panel.clear()
    self.content_panel.add_component(DashboardPage())
    pass

  def visions_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.content_panel.clear()
    self.content_panel.add_component(VisionsPage())
    pass
