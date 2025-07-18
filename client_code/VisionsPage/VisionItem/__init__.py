from ._anvil_designer import VisionItemTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class VisionItem(VisionItemTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def open_vision_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.parent.raise_event('x-manage-vision', vision=self.item)
    pass

  def delete_vision_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    if confirm(f"Are you sure you want to delete {self.item['vision_name']}?"):
      self.parent.raise_event('x-delete-vision', vision=self.item)
    pass
