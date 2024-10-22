# Bring in lightweight dependencies
from fastapi import FastAPI , Query 
from pydantic import BaseModel
import joblib
import numpy as np 
# import pandas as pd
from typing import Annotated 
# env name heroku-no-docker 
app = FastAPI()

class ValuesInput(BaseModel):
    value1: Annotated[float, Query(gt=0)]
    value2: Annotated[float, Query(gt=0)]
    value3: Annotated[float, Query(gt=0)]
    value4: Annotated[float, Query(gt=0)]

    class Config:
        extra = "forbid"
model_version='0.1.0'
model_path=f'trained_pipeline-{model_version}.joblib'
model = joblib.load(model_path)

classes = ["setosa", "versicolor", "virginica"]

def predict_pipeline(payload):

    input_values = np.array(
        [[payload.value1, payload.value2, payload.value3, payload.value4]],
        dtype=np.float16,
    )

    result = classes[int(model.predict(input_values)[0])]

    return result


class PredictionOut(BaseModel):
    class_name: str

@app.get("/")
async def home():
    return {"health_check": "OK", "model_version": model_version}

@app.post("/predict", response_model=PredictionOut)
async def predict(payload: ValuesInput):
    result = predict_pipeline(payload)
    return {"class_name": result}