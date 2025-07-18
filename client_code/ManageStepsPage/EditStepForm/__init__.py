from ._anvil_designer import EditStepFormTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class EditStepForm(EditStepFormTemplate):
  def __init__(self, step, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.item = step
    self.step_name_input.text = step['step_name']
    self.step_description_input.text = step['step_description']

    # Any code you write here will run before the form opens.

  def confirm_edits_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.item['step_name'] != self.step_name_input.text or self.item['step_description'] != self.step_description_input.text:
      given_input = []
      given_input.append(self.step_name_input.text)
      given_input.append(self.step_description_input.text)
      self.raise_event("x-close-alert", value=given_input)
    else:
      self.raise_event("x-close-alert", value=None)
    pass
