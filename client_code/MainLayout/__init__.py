from ._anvil_designer import MainLayoutTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..VisionsPage import VisionsPage
from ..DashboardPage import DashboardPage

class MainLayout(MainLayoutTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # self.logged_in_text.text = "Logged in as " + anvil.users.get_user()['email']

    # Any code you write here will run before the form opens.

  def logout_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.users.logout()
    open_form('Login')
    pass

  def dashboard_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('DashboardPage')
    pass

  def visions_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('VisionsPage')
    pass
