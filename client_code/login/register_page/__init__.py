from ._anvil_designer import register_pageTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class register_page(register_pageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def register_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    print("Registering User: "+ self.email_field)
    pass
