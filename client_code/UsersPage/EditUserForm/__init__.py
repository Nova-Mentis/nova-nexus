from ._anvil_designer import EditUserFormTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class EditUserForm(EditUserFormTemplate):
  def __init__(self, user, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.user = user
    self.first_name_input.text = self.user['first_name']
    self.last_name_input.text = self.user['last_name']
    self.email_input.text = self.user['email']
    
    user_roles = anvil.server.call('get_user_roles')
    self.role_dropdown.items = user_roles
    self.role_dropdown.selected_value = self.user['role']

    tenant_list = anvil.server.call('get_tenants')
    self.tenant_dropdown.items = tenant_list
    self.tenant_dropdown.selected_value = self.user['assigned_tenant'] 

    # Any code you write here will run before the form opens.

  def save_user_edits_btn_click(self, **event_args):
    """This method is called when the Save button is clicked"""
  
    updates = {}
  
    # Compare and collect changes
    if self.first_name_input.text != self.user['first_name']:
      updates['first_name'] = self.first_name_input.text
  
    if self.last_name_input.text != self.user['last_name']:
      updates['last_name'] = self.last_name_input.text
  
    if self.email_input.text != self.user['email']:
      updates['email'] = self.email_input.text
  
      # Handle role change (compare by role_name)
    if self.role_dropdown.selected_value['role_name'] != self.user['role']['role_name']:
      updates['role'] = {'role_name': self.role_dropdown.selected_value['role_name']}
  
      # Handle tenant change (compare by tenant_name)
    if self.tenant_dropdown.selected_value['tenant_name'] != self.user['assigned_tenant']['tenant_name']:
      updates['tenant'] = {'tenant_name': self.tenant_dropdown.selected_value['tenant_name']}
  
    if not updates:
      alert("No changes detected.")
      return
  
      # Call updated server function with the primary key email and only changed fields
    result = anvil.server.call('update_user_profile', email=self.user['email'], updates=updates)
  
    if not result:
      alert("An error occurred when updating the user")
  
    self.raise_event("x-close-alert", value=42)

  def cancel_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.raise_event("x-close-alert", value=42)
    pass
