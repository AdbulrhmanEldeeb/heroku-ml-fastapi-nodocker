from typing import Annotated  # Annotated for enforcing input validation rules
from pydantic import BaseModel  # BaseModel for request validation
from fastapi import Query  #   Query for validation


# Define the input schema for the API with validation rules
class ValuesInput(BaseModel):
    # The four input values, each of which must be a positive float
    value1: Annotated[float, Query(gt=0)]
    value2: Annotated[float, Query(gt=0)]
    value3: Annotated[float, Query(gt=0)]
    value4: Annotated[float, Query(gt=0)]

    class Config:
        # Prevent extra fields from being passed
        extra = "forbid"


# Define the output schema for the API
class PredictionOut(BaseModel):
    class_name: str  # The predicted Iris species class name
