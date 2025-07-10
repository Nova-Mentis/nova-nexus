from ._anvil_designer import CreateStepsPageTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .CustomStepForm import CustomStepForm

class CreateStepsPage(CreateStepsPageTemplate):
  def __init__(self, vision, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.vision_name_label.text = vision['vision_name']

    # Any code you write here will run before the form opens.

  def add_custom_step_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    alert(CustomStepForm, large=True)
    pass
