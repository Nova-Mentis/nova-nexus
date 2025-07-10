from ._anvil_designer import VisionsPageTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import State

class VisionsPage(VisionsPageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.vision_repeating_panel.items = anvil.server.call('get_visions_list', user=anvil.users.get_user(), tenant=State.tenant)
    

    # Any code you write here will run before the form opens.

  def vision_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('CreateVisionPage')
    pass
