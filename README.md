# FastAPI Backend for Multinomial NB Classifier

This repository contains a simple backend service that demonstrates how to serve a trained machine learning model using FastAPI. I've developed this project to showcase the deployment of a Multinomial Naive Bayes classifier trained on the 20Newsgroups dataset (from scikit-learn).

## 1. Project Overview

The goal of this project is to illustrate how a machine learning model can be integrated into a web application. The model is serialized using joblib and served through FastAPI, making it accessible via a RESTful API.

## 2. Key Components

* **Model:** The classifier predicts the category of text input, leveraging a Multinomial Naive Bayes model trained on the 20Newsgroups dataset (from scikit-learn).
* **FastAPI:** A modern, fast web framework used to build the API endpoints.
* **Serialization:** The trained model and category labels are stored in a joblib file for efficient loading and usage.
* **Caching:** Response caching is implemented using joblib.Memory to speed up repeated requests.
* **Data Validation:** Pydantic is used for validating input data and ensuring type safety.

## 3. Project Structure

* **main.py:** Contains the FastAPI setup and endpoint definitions.
* **schemas.py:** Defines Pydantic models for input and output data.
* **predict.py:** Handles model loading and prediction logic.

## 4. How It Works

* **Model Loading:** The model and category labels are loaded from a joblib file (newsgroups_model.joblib) when the application starts.
* **Prediction Endpoint:** The `/prediction` endpoint accepts a JSON payload with the text to classify and returns the predicted category.
* **Caching Mechanism:** Predictions are cached to reduce computation time for repeated requests. The cache can be cleared using the `/cache` endpoint.

## 5. Running the Application

### 5.1 Using Docker

* **Build the docker image:**
  
  ```bash
  docker-compose build```

* **Run the docker container:**

  ```bash
  docker-compose up```

This will start the application on http://0.0.0.0:8000. You can access the interactive API documentation at http://localhost:8000/docs.

### 5.2 Without Using Docker

If you prefer to run the application without Docker, ensure you have Python 3.9.7 installed, then install the required packages and start the application:

* **Install Dependencies:**

  ```bash
  pip install -r requirements.txt```

* **Start the Application:**

  ```bash
  uvicorn app.main:app --reload```

Visit http://127.0.0.1:8000/docs to explore the API documentation and test the endpoints.



