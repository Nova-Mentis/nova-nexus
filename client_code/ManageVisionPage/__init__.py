from ._anvil_designer import ManageVisionPageTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .VisionOverview import VisionOverview

class ManageVisionPage(ManageVisionPageTemplate):
  def __init__(self, vision, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.current_vision = vision
    self.vision_name_label.text = self.current_vision['vision_name']
    self.vision_statement_label.text = self.current_vision['vision_statement']
    # Any code you write here will run before the form opens.

  def manage_steps_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('ManageStepsPage', vision=self.current_vision)
    pass
