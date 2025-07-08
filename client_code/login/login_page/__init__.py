from ._anvil_designer import login_pageTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class login_page(login_pageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def login_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    print("Logging in User: "+ self.email_field.text)

    if self.email_field.text != "" :
      self.email_warn_label.text = "Please enter in your email"
      self.email_warn_label.visible = True
    pass

  def register_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass
