from ._anvil_designer import MainLayoutTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..VisionsPage import VisionsPage
from ..DashboardPage import DashboardPage
from anvil.designer import in_designer
if not in_designer:
  import anvil.tz

class MainLayout(MainLayoutTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    '''
    try:
      anvil.server.call('server_heartbeat')
    except anvil.server.SessionExpiredError:
      anvil.server.reset_session()
      anvil.server.call('set_up_session')
    '''
  
    # Set Tenant
    tenant_list = anvil.server.call("get_tenants")
    self.tenant_dropdown.items = tenant_list
    if anvil.server.call('get_session_tenant') is not None:
      self.tenant_dropdown.selected_value = anvil.server.call('get_session_tenant')
    else:
      anvil.server.call('switch_session_tenant', self.tenant_dropdown.selected_value)

    # Set Visibility for Admins
    current_user_role = anvil.users.get_user()['role']['role_name']
    print("User role is " + current_user_role)
    if current_user_role == "super_admin":
      self.tenant_dropdown.visible = True
      self.user_link.visible = True
      self.system_link.visible = True
      self.tenant_manager_link.visible = True
      self.resources_link.visible = True
    elif current_user_role == "admin":
      self.tenant_dropdown.visible = False
      self.user_link.visible = True
      self.system_link.visible = True
      self.tenant_manager_link.visible = False
      self.resources_link.visible = True
    else:
      self.tenant_dropdown.visible = False
      self.user_link.visible = False
      self.system_link.visible = False
      self.tenant_manager_link.visible = False
      self.resources_link.visible = False


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
    anvil.server.call('switch_session_tenant', tenant=self.tenant_dropdown.selected_value)
    print("Selected Tenant is now " + self.tenant_dropdown.selected_value['tenant_name'])
    open_form('DashboardPage')
    pass

  def user_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('UsersPage')
    pass

  def resources_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('ResourcesPage')
    pass

  def system_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('TenantSettingsPage')
    pass

  def tenant_manager_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('TenantManagerPage')
    pass
