from ._anvil_designer import ChosenStepItemTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class ChosenStepItem(ChosenStepItemTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def remove_step_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    if confirm("Are you sure you wan to remove this step?"):
      self.parent.raise_event('x-remove-step', step=self.item)
    pass
