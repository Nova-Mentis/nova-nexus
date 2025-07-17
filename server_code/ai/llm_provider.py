import anvil.secrets
from pydantic_ai.providers.openai import OpenAIProvider

# Retrieve your secret key from Anvil Secrets
OPENAI_KEY = anvil.secrets.get_secret("OPENAI_API_KEY")

# Instantiate the OpenAI provider using the key
openai_provider = OpenAIProvider(api_key=OPENAI_KEY)
