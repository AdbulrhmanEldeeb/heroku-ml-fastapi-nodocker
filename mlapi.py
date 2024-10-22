# Import necessary dependencies
from fastapi import FastAPI, Query  # FastAPI for building the web app,
import joblib  # joblib for loading the trained model
import numpy as np  # numpy for numerical operations
from models import ValuesInput, PredictionOut  # validation classes

# Initialize FastAPI app
app = FastAPI()


def predict_pipeline(payload):
    # Convert the input data into a NumPy array with the appropriate shape
    input_values = np.array(
        [[payload.value1, payload.value2, payload.value3, payload.value4]],
        dtype=np.float16,  # Use float16 to conserve memory
    )

    # Make a prediction using the trained model and return the corresponding class label
    result = classes[int(model.predict(input_values)[0])]

    return result


# Define the version and load the trained model
model_version = "0.1.0"
model_path = f"trained_pipeline-{model_version}.joblib"  # Path to the trained model
model = joblib.load(model_path)  # Load the model using joblib


# Class labels corresponding to Iris species
classes = ["setosa", "versicolor", "virginica"]

# Define a function to make predictions using the input data


# Health check endpoint to verify the API is running
@app.get("/")
async def home():
    return {"health_check": "OK", "model_version": model_version}


# Endpoint to receive input data and return the predicted Iris species
@app.post("/predict", response_model=PredictionOut)
async def predict(payload: ValuesInput):
    # Call the predict function to get the prediction result
    result = predict_pipeline(payload)

    # Return the prediction in the response
    return PredictionOut(class_name=result)
