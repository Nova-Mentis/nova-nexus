from ._anvil_designer import ManageVisionPageTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .EditVisionNameForm import EditVisionNameForm
from .EditVisionStatementForm import EditVisionStatementForm

class ManageVisionPage(ManageVisionPageTemplate):
  def __init__(self, vision, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.item = vision
    # Any code you write here will run before the form opens.

  def manage_steps_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('ManageStepsPage', vision=self.item)
    pass

  def manage_questions_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('ManageQuestionsPage', vision=self.item)
    pass

  def manage_tiers_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('ManageVisionTiersPage', vision=self.item)
    pass

  def edit_vision_name_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    new_vision_name = alert(content=EditVisionNameForm(vision=self.item), buttons="")
    if new_vision_name is not None:
      anvil.server.call('update_vision', 
                        vision_id=self.item['vision_id'],
                        vision_name=new_vision_name
                      )
      self.refresh_labels()
    pass

  def refresh_labels(self):
    self.item = anvil.server.call('get_vision', vision_id=self.item['vision_id'])
    self.refresh_data_bindings()

  def edit_statement_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    new_vision_statement = alert(content=EditVisionStatementForm(vision=self.item), buttons="")
    if new_vision_statement is not None:
      anvil.server.call('update_vision', 
                        vision_id=self.item['vision_id'],
                        vision_statement=new_vision_statement
                      )
      self.refresh_labels()
    pass

