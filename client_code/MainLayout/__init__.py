from ._anvil_designer import MainLayoutTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..VisionsPage import VisionsPage
from ..DashboardPage import DashboardPage
from .. import State

class MainLayout(MainLayoutTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # self.logged_in_text.text = "Logged in as " + anvil.users.get_user()['email']

    # Setup up super admin and admin view

    #Super Admin
    # Tenant Drop Down
    current_user = anvil.users.get_user()
    
    try:
      is_super_admin = anvil.server.call("is_super_admin", current_user)
      tenant_list = anvil.server.call("get_tenants")
    except anvil.server.SessionExpiredError:
      anvil.server.reset_session()
      print("Resetting session as it has expired")
      is_super_admin = anvil.server.call("is_super_admin", current_user)
      tenant_list = anvil.server.call("get_tenants")

    # Set Tenant
    self.tenant_dropdown.items = tenant_list
    if State.tenant is not None:
      self.tenant_dropdown.selected_value = State.tenant
    else:
      State.tenant = self.tenant_dropdown.selected_value
    print("Selected Tenant is now " + self.tenant_dropdown.selected_value['tenant_name'])

    if is_super_admin:
      self.tenant_dropdown.visible = True
      self.user_link.visible = True
    else:
      self.tenant_dropdown.visible = False

    # Admin

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

  def profile_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('UserProfilePage')
    pass

  def tenant_dropdown_change(self, **event_args):
    """This method is called when an item is selected"""
    State.tenant = self.tenant_dropdown.selected_value
    print("Selected Tenant is now " + self.tenant_dropdown.selected_value['tenant_name'])
    open_form('DashboardPage')
    pass
