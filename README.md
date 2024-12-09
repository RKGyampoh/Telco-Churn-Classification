Telco Customer Churn Prediction App

This project is a Streamlit-based web application designed to predict customer churn for a telecom company using multiple machine learning models.

The app provides a simple and interactive interface for users to input customer data and view churn predictions.

Table of Contents

Overview

Features

Directory Structure

Setup Instructions

Usage

Models

Contributing

License

Overview

Customer churn prediction is critical for businesses to retain customers and minimize revenue loss. This application uses machine learning models trained on telco customer data to provide predictions and insights. It includes a pre-processing pipeline and multiple classification models to analyze customer behavior.

Features

Interactive Interface: Built using Streamlit, offering a simple layout for predictions.

Multi-Model Prediction: Supports different machine learning models such as:

Random Forest (RF)

Support Vector Machine (SVC)

Gradient Boosting (GB)

K-Nearest Neighbors (KNN)

Logistic Regression (LR)

Bagging Classifier

Preprocessing Pipeline: Automates data preprocessing, including encoding and scaling.

Directory Structure

bash

Telco/

├── data/

│ └── telco_churn_model.pkl # Example dataset

├── models/

│ ├── pipeline.pkl # Preprocessing pipeline

│ ├── premode.pkl # Saved preprocessing logic

│ ├── RF_model.pkl # Random Forest model

│ ├── SVC_model.pkl # Support Vector Classifier model

│ ├── GB_model.pkl # Gradient Boosting model

│ ├── LR_model.pkl # Logistic Regression model

│ ├── KNN_model.pkl # K-Nearest Neighbors model

│ ├── Bagging_classifier_model.pkl # Bagging Classifier model

├── Scripts/

│ ├── app.py # Main Streamlit app file

│ ├── home.py # Home page layout

│ ├── data.py # Data processing script

│ ├── prediction.py # Prediction functionality

│ ├── dashboard.py # Dashboard integration (optional)

├── pyvenv.cfg # Virtual environment configuration

Setup Instructions

Clone the Repository:

bash

git clone https://github.com/yourusername/Telco-churn-classification.git

cd Telco

Create and Activate a Virtual Environment:

bash python -m venv venv

source venv/bin/activate # On macOS/Linux

venv\Scripts\activate # On Windows

Install Dependencies:

bash

pip install -r requirements.txt

Run the App:

bash

streamlit run app.py

Usage

Launch the app in your browser.

Navigate to the Predict Page using the sidebar.

Input customer data into the provided fields.

Submit the form to view churn prediction results and probabilities.

Models

The following machine learning models are included:

Random Forest (RF): A robust ensemble model.

Support Vector Machine (SVC): Suitable for high-dimensional data.

Gradient Boosting (GB): For accurate predictions on small datasets.

Logistic Regression (LR): A simple and interpretable model.

K-Nearest Neighbors (KNN): For instance-based learning.

Bagging Classifier: Combines the predictions of multiple base learners.

All models are pre-trained and stored in the models/ directory. The app dynamically loads the model pipeline and pre-trained models using pickle.

Contributing

Contributions are welcome! Please:

Fork the repository.

Create a new branch for your feature or bug fix.

Submit a pull request for review.

License

This project is licensed under the MIT License.
