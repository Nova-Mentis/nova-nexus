from ._anvil_designer import CreateVisionPageTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

vision_guidance_level = ""

class CreateVisionPage(CreateVisionPageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Setup form options
    # Vision Types
    self.vision_type_dropdown.items = anvil.server.call('get_vision_types')
    self.questions_panel.items = anvil.server.call('get_questions_for_vision_type', self.vision_type_dropdown.selected_value)

  def set_panel_visibility(self):
    self.type_column_panel.visible = True
    self.guided_questions_panel.visible = False
    self.rough_idea_panel.visible = False
    self.custom_vision_statement_panel.visible = False
    if self.vision_guidance_level == "Guided":
      self.guided_questions_panel.visible = True
      self.guide_questions_by_vision_type_panel.visible = True
      self.rough_idea_panel.visible = False
      self.custom_vision_statement_panel.visible = False
    elif self.vision_guidance_level == "Assisted":
      self.guided_questions_panel.visible = False
      self.rough_idea_panel.visible = True
      self.custom_vision_statement_panel.visible = False
    else:
      self.guided_questions_panel.visible = False
      self.rough_idea_panel.visible = False
      self.custom_vision_statement_panel.visible = True
    pass
    

  def guided_vision_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.vision_guidance_level = "Guided"
    self.set_panel_visibility()
    pass

  def custom_vision_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.vision_guidance_level = "Custom"
    self.set_panel_visibility()
    pass

  def rough_idea_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.vision_guidance_level = "Assisted"
    self.set_panel_visibility()
    pass

  def create_custom_vision_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    created_vision_id = anvil.server.call('create_vision', 
                      vision_name=self.custom_vision_name_input.text, 
                      vision_statement=self.custom_vision_statement_input.text, 
                      user=anvil.users.get_user(), 
                      vision_type=self.vision_type_dropdown.selected_value,
                      tenant=anvil.server.call('get_cookies_tenant')
                     )
    created_vision = anvil.server.call('get_vision', vision_id=created_vision_id)
    open_form('ManageStepsPage', vision=created_vision)
    pass

  def vision_type_dropdown_change(self, **event_args):
    """This method is called when an item is selected"""
    if self.vision_type_dropdown.selected_value['vision_type_name'] == "Other":
      print("Other choice made, setting up rough idea for questions to ask")
      self.guide_questions_by_vision_type_panel.visible = False
      self.other_category_guided_option_panel.visible = True
    else:
      print("Setting questions to " + self.vision_type_dropdown.selected_value['vision_type_name'])
      self.guide_questions_by_vision_type_panel.visible = True
      self.other_category_guided_option_panel.visible = False
      self.questions_panel.items = anvil.server.call('get_questions_for_vision_type', self.vision_type_dropdown.selected_value)
    pass

  def confirm_answers_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass




      
    
