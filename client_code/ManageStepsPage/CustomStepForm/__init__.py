from ._anvil_designer import CustomStepFormTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class CustomStepForm(CustomStepFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def confirm_add_custom_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    given_input = []
    given_input.append(self.step_name_input.text)
    given_input.append(self.step_description_input.text)
    self.raise_event("x-close-alert", value=given_input)
    pass
