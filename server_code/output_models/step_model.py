from pydantic import BaseModel
from typing import List

class Step(BaseModel):
  name: str
  description: str

class StepModel(BaseModel):
  steps: List[Step]
