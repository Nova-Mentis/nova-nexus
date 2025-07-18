from ._anvil_designer import ManageQuestionsPageTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class ManageQuestionsPage(ManageQuestionsPageTemplate):
  def __init__(self, vision, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.item = vision
    self.main_label.text = ("Manage Questions for " + vision['vision_name'])

    # Any code you write here will run before the form opens.
