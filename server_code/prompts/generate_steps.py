
def generate_steps_prompt(vision):
  vision_statement = vision['vision_statement']
  return (
    f"Given the following vision statement:\n\n\"{vision_statement}\"\n\n"
    "Generate 5 steps needed to achieve the vision."
    "Steps can we defined as the skills that need to be learnt, the obstacles they need to overcome, or things that need to be achieved. "
    "Ensure each step includes a step_name and a step_description"
  )
