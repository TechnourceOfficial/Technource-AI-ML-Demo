# AI ML Demo

This demo will predict user's favourite Music & Will Buy inusrance or not by the age.
Also it will show user's diet for the full day by hight, weight and age.

## File Structure

    ├── prediction_master           # Music & Insurance csv file generation, model creation and model use functions
        ├── music                   # Music prediction master
            ├── csv_create          # Generate music training data
            ├── model_create        # Model creation with trained data
            ├── test_prediction     # Function for predict user's favourite music as per the age
            ├── model               # Trained model
            ├── music.csv           # Training data CSV
        ├── insurance               # Insurance prediction master
            ├── csv_create          # Generate insurance training data
            ├── model_create        # Model creation with trained data
            ├── test_prediction     # Function for predict user's favourite insurance as per the age
            ├── model               # Trained model
            ├── insurance.csv       # Training data CSV
    ├── prediction_setup            # Generated trained CSV and model for Music & Insurance
    ├── app                         # Python application
    └── README.md

## Python Version
3.12.4

## Used Packages

### random
pip install random
Used for get random data from the list, range .... etc
### csv
Used for generate CSV files with random data
### pandas
pip install pandas
Used for read CSV files
### scikit-learn (sklearn)
pip install scikit-learn
Used for train model and make it for predict
### joblib
pip install joblib
Used for create joblib file of the model for use directly
### flask
pip install flask
Framework used for frontend part
### openai
pip install openai
Used for get AI result of requested prompt

## Available Scripts

In the project directory, you can run:

### `python prediction_setup.py`

Prepare trained Music & Insurance model

### `python -m flask run`
Runs the app in the development mode.\
Open [http://localhost:5000](http://localhost:5000) to view it in your browser