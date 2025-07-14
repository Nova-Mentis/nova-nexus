from ._anvil_designer import DashboardPageTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import State

class DashboardPage(DashboardPageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.num_visions_card_label.text = anvil.server.call('count_visions', user=anvil.users.get_user(), tenant=State.tenant)

    # Any code you write here will run before the form opens.
