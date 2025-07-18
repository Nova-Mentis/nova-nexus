from ._anvil_designer import UserItemTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class UserItem(UserItemTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.role_label.text = self.item['role']['role_name']
    self.add_event_handler('x-edits-made-to-user', self.handle_edits_made_to_user)
    # Any code you write here will run before the form opens.

  def edit_user_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.parent.raise_event('x-edit-user', user=self.item)
    pass

  def handle_edits_made_to_user(self):
    self.parent.raise_event('x-refresh-user-list')
    pass
