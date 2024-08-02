# FastAPI Backend for Multinomial NB Classifier

This repository contains a simple backend service that demonstrates how to serve a trained machine learning model using FastAPI. I've developed this project to showcase the deployment of a Multinomial Naive Bayes classifier trained on the 20Newsgroups dataset.

## Project Overview
The goal of this project is to illustrate how a machine learning model can be integrated into a web application. The model is serialized using joblib and served through FastAPI, making it accessible via a RESTful API.

## Key Components
* **Model:** The classifier predicts the category of text input, leveraging a Multinomial Naive Bayes model trained on the 20Newsgroups dataset.
* **FastAPI:** A modern, fast web framework used to build the API endpoints.
* **Serialization:** The trained model and category labels are stored in a joblib file for efficient loading and usage.
* **Caching:** Response caching is implemented using joblib.Memory to speed up repeated requests.
* **Data Validation:** Pydantic is used for validating input data and ensuring type safety.

## Project Structure
* **main.py:** Contains the FastAPI setup and endpoint definitions.
* **schemas.py:** Defines Pydantic models for input and output data.
* **predict.py:** Handles model loading and prediction logic.

## How It Works
* **Model Loading:** The model and category labels are loaded from a joblib file (newsgroups_model.joblib) when the application starts.
* **Prediction Endpoint:** The `/prediction` endpoint accepts a JSON payload with the text to classify and returns the predicted category.
* **Caching Mechanism:** Predictions are cached to reduce computation time for repeated requests. The cache can be cleared using the `/cache` endpoint.

## Running the Application

### Using Docker

* Build the docker image
  ```bash
  docker-compose build```
