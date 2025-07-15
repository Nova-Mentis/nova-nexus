from ._anvil_designer import ManageStepsPageTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .CustomStepForm import CustomStepForm

class ManageStepsPage(ManageStepsPageTemplate):
  def __init__(self, vision, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.main_label.text = "Manage Vision Steps for " + vision['vision_name']
    self.manage_steps_top_panel.add_event_handler('x-add-step', self.handle_add_step)

    # Any code you write here will run before the form opens.

  def add_custom_step_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    alert(content=CustomStepForm(), 
          large=True,
          buttons=""
         )
    pass

  def handle_add_step(self, step_name, step_description, **event_args):
    print("Adding new step")
    pass
