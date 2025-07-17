import anvil.secrets
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from pydantic import BaseModel

from .llm_provider import openai_provider  # Import the shared provider
from .output_models import all_models
from .prompts import all_prompts

'''
Example Client Usage

# For a fixed prompt
result = anvil.server.call("ask_model", {
    "prompt_key": "generate_user_info",
    "output_model": "UserInfo"
})

# For a dynamic prompt
result = anvil.server.call("ask_model", {
    "prompt_key": "create_vision_scorecard",
    "prompt_args": {
        "vision": "I want to live a life of creativity and connection through music and storytelling."
    },
    "output_model": "VisionScorecard"
})
'''

def send_prompt(
  prompt: str,
  *,
  model_name: str = "gpt-4.1-mini",
  output_model: type[BaseModel] | None = None,
  temperature: float = 0.7,
  max_tokens: int = 512,
):
  model = OpenAIModel(
    model_name,
    provider=openai_provider,
    settings={"temperature": temperature, "max_tokens": max_tokens},
  )
  agent = Agent(model, output_type=output_model)
  result = agent.run_sync(prompt)
  return result.output


@anvil.server.callable
def agent_request(payload: dict):
  prompt_name = payload.get("prompt_key")  # Lookup key, not raw string!
  output_model_name = payload.get("output_model")
  model_name = payload.get("model", "gpt-4.1-mini")
  temperature = payload.get("temperature", 0.7)
  max_tokens = payload.get("max_tokens", 512)

  # Resolve prompt function and model class
  prompt_func = all_prompts.get(prompt_name)
  if prompt_func is None:
    raise ValueError(f"Unknown prompt key: {prompt_name}")
  prompt = prompt_func(**payload.get("prompt_args", {}))

  output_model_class = all_models.get(output_model_name)

  return send_prompt(
    prompt,
    model_name=model_name,
    output_model=output_model_class,
    temperature=temperature,
    max_tokens=max_tokens,
  )