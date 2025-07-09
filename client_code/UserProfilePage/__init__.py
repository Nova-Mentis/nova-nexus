from ._anvil_designer import UserProfilePageTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class UserProfilePage(UserProfilePageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Set input and email fields
    current_user = anvil.users.get_user()
    current_user_first_name = current_user['first_name'] if current_user else ""
    current_user_last_name = current_user['last_name'] if current_user else ""
    current_user_email = current_user['email'] if current_user else ""
    self.first_name_input.text = current_user_first_name
    self.last_name_input.text = current_user_last_name
    self.email.text = current_user_email

    # Any code you write here will run before the form opens.

  def save_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    update_result = anvil.server.call('update_user_profile', self.first_name_input.text, self.last_name_input.text, self.email.text)
    if update_result:
      alert("Updated Successfully")
    else:
      alert("Something Went Wrong")
    pass
