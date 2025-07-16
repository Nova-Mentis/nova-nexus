from ._anvil_designer import EvaluateVisionPageTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil.designer import in_designer
if in_designer:
  anvil.server.reset_session()

class EvaluateVisionPage(EvaluateVisionPageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
