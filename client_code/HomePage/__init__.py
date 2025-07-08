#from ._anvil_designer import HomePageTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
#from ..VisionsPage import VisionsPage
#from ..DashboardPage import DashboardPage

class HomePage(HomePageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.profile_btn.text = anvil.users.get_user()['email']

    # Any code you write here will run before the form opens.

  def visions_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    pass

  def dashboard_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    pass

  def logout_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.users.logout()
    open_form('Login')
    pass

  def profile_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass
