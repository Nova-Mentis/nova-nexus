'''
from .user import UserInfo
from .vision import VisionScorecard  # Add more as needed

# Registry of available models (string → class)
all_models = {
    "UserInfo": UserInfo,
    "VisionScorecard": VisionScorecard,
}


Example Uer
# output_models/user.py

from pydantic import BaseModel

class UserInfo(BaseModel):
    name: str
    email: str
    age: int
'''

from .step_model import StepModel

all_models = {
  "StepModel": StepModel
}
