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
    self.first_name_input.text = user['first_name']
    self.last_name_input.text = user['last_name']
    self.email_input.text = user['email']
    
    user_roles = anvil.server.call('get_user_roles')
    self.role_dropdown.items = user_roles

    tenant_list = anvil.server.call('get_tenants')
    self.tenant_dropdown.items = tenant_list

    # Any code you write here will run before the form opens.

  def save_user_edits_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    # Save Method
    result = anvil.server.call('update_user_profile',
                      first_name=self.first_name_input.text,
                      last_name=self.last_name_input.text,
                      email=self.email_input.text,
                      role=self.role_dropdown.selected_value,
                      tenant=self.tenant_dropdown.selected_value                     
                     )
    if result:
      self.parent.raise_event('x-edits-made-to-user')
    else:
      alert("An error occurred when updating the user")
    self.raise_event("x-close-alert", value=42)
    pass

  def cancel_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.raise_event("x-close-alert", value=42)
    pass
