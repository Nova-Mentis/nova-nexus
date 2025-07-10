from ._anvil_designer import ViewVisionPageTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .VisionOverview import VisionOverview
from .VisionSteps import VisionSteps

class ViewVisionPage(ViewVisionPageTemplate):
  def __init__(self, vision, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.vision_name_label.text = vision["vision_name"]
    self.vision_component_dropdown.items = anvil.server.call('get_vision_components')
    self.content_panel.add_component(VisionOverview())
    # Any code you write here will run before the form opens.

  def vision_component_dropdown_change(self, **event_args):
    """This method is called when an item is selected"""
    self.content_panel.clear()
    selected_vision_component = self.vision_component_dropdown.selected_value['vision_component']
    print("Selected Vision Component is " + selected_vision_component)
    if selected_vision_component == "Overview":
      self.content_panel.add_component(VisionOverview())
    if selected_vision_component == "Steps":
      self.content_panel.add_component(VisionSteps())
    pass
