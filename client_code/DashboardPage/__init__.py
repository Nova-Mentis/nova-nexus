from ._anvil_designer import DashboardPageTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class DashboardPage(DashboardPageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.refresh_cards()

    # Any code you write here will run before the form opens.

  def refresh_cards(self):
    self.num_visions_card_label.text = anvil.server.call('count_visions', user=anvil.users.get_user(), tenant=anvil.server.call('get_cookies_tenant'))
