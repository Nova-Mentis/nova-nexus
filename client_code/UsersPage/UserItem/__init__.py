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
    self.user_name_label = self.user['first_name']
    self.user_email_name = self.user['email']

    # Any code you write here will run before the form opens.
