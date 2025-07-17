
def generate_steps_prompt(vision, existing_steps):
  vision_statement = vision['vision_statement']

  # Extract step names
  existing_step_names = [step['name'] for step in existing_steps if step and 'name' in step]
  existing_list = "\n- " + "\n- ".join(existing_step_names) if existing_step_names else "None"

  return f"""Given the following vision statement:

"{vision_statement}"

Generate 5 new and unique steps that will help achieve this vision.

Steps may include:
- Skills the person needs to learn
- Obstacles they need to overcome
- Milestones they need to achieve

Each step should include a concise **name** and a 1–2 sentence **description**.

Please **do not include** any of the following existing steps:
{existing_list}
"""
