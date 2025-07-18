from ._anvil_designer import EditVisionStatementFormTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class EditVisionStatementForm(EditVisionStatementFormTemplate):
  def __init__(self, vision, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.item = vision
    self.refresh_data_bindings()

    # Any code you write here will run before the form opens.

  def save_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.item['vision_statement'] != self.vision_statement_input.text:
      self.raise_event("x-close-alert", value=self.vision_statement_input.text)
    else:
      self.raise_event("x-close-alert", value=None)
    pass
