# Iris Classification API - FastAPI Deployment on Heroku with no docker usage

This project implements a simple API to classify Iris flower species using FastAPI and a pre-trained machine learning model. The application is deployed on Heroku and can be used to predict the species of an Iris flower based on input measurements.

## Features
- API built using FastAPI.
- Predicts Iris species: Setosa, Versicolor, and Virginica.
- Deployed on Heroku for easy access.

 
## Deployment: 
the app was deployed to this url using heroku :

https://iris-no-docker0121-fc181488f5b1.herokuapp.com/ 

heroku repo :

https://git.heroku.com/iris-no-docker0121.git

## API Endpoints
#### GET /: Health check endpoint:

https://iris-no-docker0121-fc181488f5b1.herokuapp.com/ 

Returns the current status and model version.

Example response:

```json
{
  "health_check": "OK",
  "model_version": "0.1.0"
}
```
#### POST /predict: Predict the Iris species.

https://iris-no-docker0121-fc181488f5b1.herokuapp.com/predict 

Request body:
```json
{
  "value1": 5.1,
  "value2": 3.5,
  "value3": 1.4,
  "value4": 0.2
}
```
Example response:

```json
{
  "class_name": "setosa"
}
```

