from ._anvil_designer import GeneratedStepItemTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class GeneratedStepItem(GeneratedStepItemTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.generated_step_name_label.text = self.item['name']
    self.generate_step_description_label.text = self.item['description']
    # Any code you write here will run before the form opens.

  def add_generated_step_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    generated_step = {
      "name": self.item['name'],
      "description": self.item['description']
    }
    self.parent.raise_event('x-add-generated-step', generated_step=generated_step)
    pass
