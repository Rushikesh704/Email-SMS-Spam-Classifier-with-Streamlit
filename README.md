# Email-SMS-Spam-Classifier-with-Streamlit

This project is a simple web application built with Streamlit for classifying email or SMS messages as spam or not spam using a pre-trained machine learning model.

## Overview

The application provides a user-friendly interface where users can input a message, and the model predicts whether the message is spam or not spam. It employs text preprocessing techniques such as tokenization, stopword removal, punctuation removal, and stemming to transform the input text into a format suitable for prediction.

## Installation

To run this application locally, follow these steps:

1. Clone this repository to your local machine:

2. Navigate to the project directory:

3. Install the required Python dependencies:


## Usage

To launch the application, run the following command:

streamlit run app.py

Once the application is running, open your web browser and go to the URL provided by Streamlit (usually `http://localhost:8501`). You will see the input text area where you can enter a message. Click the "Predict" button to get the prediction result, which will be displayed below the input area.


## Files

- `app.py`: The main Streamlit application file containing the code for the user interface and prediction logic.
- `model.pkl`: The pre-trained machine learning model for spam classification.
- `vectorizer.pkl`: The TF-IDF vectorizer used for text vectorization.
- `requirements.txt`: A list of Python dependencies required to run the application.


## Credits

- The model was trained using the [Spam SMS Collection](https://www.kaggle.com/uciml/sms-spam-collection-dataset) dataset from Kaggle.
