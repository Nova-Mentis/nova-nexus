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


def send_prompt(
  prompt: str,
  *,
  model_name: str = "gpt-4.1-mini",
  output_model: type[BaseModel] | None = None,
  temperature: float = 0.7,
  max_tokens: int = 512,
):
  """
    Sends a prompt to the specified OpenAI model using a structured or unstructured output.
    """
  model = OpenAIModel(
    model_name,
    provider=openai_provider,
    settings={"temperature": temperature, "max_tokens": max_tokens},
  )
  agent = Agent(model, output_type=output_model)
  result = agent.run_sync(prompt)
  return result.output


@anvil.server.callable
def ask_model(payload: dict):
  """
    Anvil callable function to send a prompt from the client.
    """
  prompt = payload["prompt"]
  model_name = payload.get("model", "gpt-4.1-mini")
  output_model_name = payload.get("output_model", None)
  temperature = payload.get("temperature", 0.7)
  max_tokens = payload.get("max_tokens", 512)

  # Optionally resolve the output model class by name if defined in this module
  output_model_class = globals().get(output_model_name)

  return send_prompt(
    prompt,
    model_name=model_name,
    output_model=output_model_class,
    temperature=temperature,
    max_tokens=max_tokens,
  )