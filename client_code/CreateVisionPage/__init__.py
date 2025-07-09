from ._anvil_designer import CreateVisionPageTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class CreateVisionPage(CreateVisionPageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Setup form options
    # Vision Types
    self.vision_type_dropdown.items = anvil.server.call('get_vision_types')

  def guided_vision_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.type_column_panel.visible = True
    self.custom_vision_statement_panel.visible = False
    pass

  def custom_vision_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.type_column_panel.visible = True
    self.custom_vision_statement_panel.visible = True
    pass

  def create_custom_vision_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('create_vision', self.custom_vision_name_input.text, self.custom_vision_statement_input.text, anvil.users.get_user(), self.vision_type_dropdown.selected_value)
    open_form('VisionsPage')
    pass
    
