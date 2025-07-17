'''
# prompts/__init__.py

from .user_prompts import generate_user_info_prompt
from .vision_prompts import create_vision_scorecard_prompt

# Registry of callable prompts by name
all_prompts = {
    "generate_user_info": generate_user_info_prompt,
    "create_vision_scorecard": create_vision_scorecard_prompt,
}
'''