from ._anvil_designer import CreateVisionPageTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import State

class CreateVisionPage(CreateVisionPageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Setup form options
    # Vision Types
    self.vision_type_dropdown.items = anvil.server.call('get_vision_types')
    self.questions_panel.items = anvil.server.call('get_questions_for_vision_type', self.vision_type_dropdown.selected_value)

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
    created_vision = anvil.server.call('create_vision', 
                      vision_name=self.custom_vision_name_input.text, 
                      vision_statement=self.custom_vision_statement_input.text, 
                      user=anvil.users.get_user(), 
                      vision_type=self.vision_type_dropdown.selected_value,
                      tenant=State.tenant
                     )
    open_form('CreateStepsPage', created_vision)
    pass

  def vision_type_dropdown_change(self, **event_args):
    """This method is called when an item is selected"""
    self.questions_panel.items = anvil.server.call('get_questions_for_vision_type', self.vision_type_dropdown.selected_value)
    self.guided_questions_panel.visible = True
    pass
    
