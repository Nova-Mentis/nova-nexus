from ._anvil_designer import ManageStepsPageTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .CustomStepForm import CustomStepForm

class ManageStepsPage(ManageStepsPageTemplate):
  def __init__(self, vision, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.current_vision = vision
    self.main_label.text = "Manage Vision Steps for " + vision['vision_name']
    self.vision_statement_label.text = vision['vision_statement']
    self.chosen_step_repeating_panel.add_event_handler('x-remove-step', self.handle_remove_step)
    self.generate_step_repeating_panel.add_event_handler('x-add-generated-step', self.handle_add_generated_step)
    self.refresh_chosen_steps()

    # Any code you write here will run before the form opens.

  def add_custom_step_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    custom_step = alert(content=CustomStepForm(), 
          large=True,
          buttons=""
         )
    anvil.server.call('add_new_step', 
                      step_name=custom_step[0], 
                      step_description=custom_step[1],
                      vision=self.current_vision,
                      ai_generated=False
                     )
    self.refresh_chosen_steps()
    pass

  def handle_remove_step(self, step, **event_args):
    anvil.server.call('remove_step', step=step)
    self.refresh_chosen_steps()
    pass

  def refresh_chosen_steps(self):
    self.chosen_step_repeating_panel.items = anvil.server.call('get_steps_list',
                                                               vision=self.current_vision
                                                              )

  def generate_steps_btn_click(self, **event_args):
    """This method is called when the button is clicked"""

    # Convert existing steps into a list of step names
    existing_steps_raw = self.chosen_step_repeating_panel.items or []
    existing_step_names = [step['step_name'] for step in existing_steps_raw]

    # Call the backend to generate steps, excluding existing ones
    gen_steps = anvil.server.call("agent_request", {
      "prompt_key": "generate_steps",
      "output_model": "StepModel",
      "prompt_args": {
        "vision": self.current_vision,
        "existing_steps": existing_step_names
      }
    })

    self.generate_step_repeating_panel.items = gen_steps["steps"]
    pass

  def handle_add_generated_step(self, generated_step, **event_args):
    # Add the step to the database via server call
    step_name = generated_step['name']
    step_description = generated_step['description']
    anvil.server.call(
      'add_new_step', 
      step_name=step_name, 
      step_description=step_description,
      vision=self.current_vision,
      ai_generated=True
    )

    # Remove the step from the generated panel
    current_items = list(self.generate_step_repeating_panel.items)
    current_items = [step for step in current_items if step['name'] != step_name]
    self.generate_step_repeating_panel.items = current_items

    # Refresh the chosen steps panel
    self.refresh_chosen_steps()
