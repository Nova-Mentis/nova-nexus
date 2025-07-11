from ._anvil_designer import VisionsPageTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import State
from .. import ViewVisionPage

class VisionsPage(VisionsPageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.refresh_vision_list()
    self.new_vision_btn.add_event_handler('x-create-vision', self.handle_create_vision)
    self.vision_data_grid.add_event_handler('x-view-vision', self.handle_view_vision)
    self.vision_data_grid.add_event_handler('x-delete-vision', self.handle_delete_vision)
    # Any code you write here will run before the form opens.


  def handle_delete_vision(self, vision, **event_args):
    print("Delete Vision event raised")
    anvil.server.call('delete_vision', vision=vision)
    self.refresh_vision_list()
    pass

  def handle_view_vision(self, vision, **event_args):
    print("View Vision event raised")
    open_form('ViewVisionPage', vision=vision)
    pass

    
  def handle_create_vision(self, **event_args):
    print("Create Vision event raised")
    open_form('CreateVisionPage')
    pass
  
  def new_vision_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.vision_btn.raise_event('x-create-vision')
    pass

  def refresh_vision_list(self):
    self.vision_repeating_panel.items = anvil.server.call('get_visions_list', user=anvil.users.get_user(), tenant=State.tenant)
