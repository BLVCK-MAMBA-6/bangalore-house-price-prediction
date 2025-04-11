# Bangalore Home Price Prediction

## Overview
This is a machine learning-based web application that predicts home prices in Bangalore based on location, square footage, number of bedrooms (BHK), and number of bathrooms. The application consists of:
- A **Flask backend** that serves an API for predictions.
- A **simple frontend** built with HTML, CSS, and JavaScript.
- A **machine learning model** (built using Jupyter Notebook) that predicts home prices based on user inputs.

## Features
- Predict home prices using machine learning.
- Search for homes by location (locations are dynamically fetched from the model).
- Simple and interactive frontend.

## Setup and Running Locally

### Prerequisites
1. Python 3
2. Flask
3. Jupyter Notebook (for running the model)
4. Other dependencies listed in `requirements.txt`

### Steps to Run Locally

1. **Clone the repository** (optional if you prefer not to clone):
    ```bash
    git clone https://github.com/yourusername/bangalore-home-price-prediction.git
    cd bangalore-home-price-prediction
    ```

2. **Install Python dependencies**:
    Create a virtual environment (optional, but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

    Then install the required Python libraries:
    ```bash
    pip install -r backend/requirements.txt
    ```

3. **Run the Flask backend**:
    Start the Flask server to serve the backend:
    ```bash
    python backend/server.py
    ```

    The backend will be accessible at `http://127.0.0.1:8080`.

4. **Open the frontend**:
    Open `frontend/index.html` in your browser to interact with the application.

## Model: `home_price_model.ipynb`
- The machine learning model for predicting home prices is built in the Jupyter Notebook `home_price_model.ipynb`.
- This notebook includes data preprocessing, feature engineering, model training, and evaluation.
- It uses a linear regression model to predict home prices based on the input features: location, square footage (`total_sqft`), number of bedrooms (`bhk`), and number of bathrooms (`bath`).
  
To run the model:
1. Install the necessary libraries:
   ```bash
   pip install -r requirements.txt
