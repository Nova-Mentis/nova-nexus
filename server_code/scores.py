import anvil.secrets
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

def create_score_id(vision, step, question, response_option):
  return f"{vision['vision_name']}_{step['step_name']}_{question['step_question']}_{response_option['response_option']}"

@anvil.server.callable
def create_score(vision, step, question, response_option):
  score_id = create_score(vision=vision, step=step, question=question, response_option=response_option)
  app_tables.question_scores.add_row(recorded_on=anvil.server.call('get_utc_time'), step=step, question=question, vision=vision, response_option=response_option, score_id=score_id)

@anvil.server.callable
def delete_score(vision=None, step=None, score_id=None):
  if score_id is not None:
    for question_scores_row in app_tables.question_scores.search(score_id=score_id):
      question_scores_row.delete()
  elif step is not None:
    for question_scores_row in app_tables.question_scores.search(step=step):
      question_scores_row.delete()
  elif vision is not None:
    for question_scores_row in app_tables.question_scores.search(vision=vision):
      question_scores_row.delete()
  else:
    print("Score not found")
