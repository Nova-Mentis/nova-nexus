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
    self.raise_event('x-add-step', 
                step_name=self.step_name_input.text, 
                step_description=self.step_description_input.text
               )
    pass
