# Author : Technource
# Date & Time : 2024/07/05 20:27
# Music CSV trained CSV file
import joblib # For load trained music file
path = "./prediction_master/music/"
# Load trained Music model
model = joblib.load(f'{path}model.joblib')
# Predict model with Male with 33 age
fav_music = model.predict([[33,1]])
if fav_music and fav_music[0]:
    print(f"Prediction for Male with age 33 favourite music: {fav_music[0]}")
else:
    print("Something went wrong with the prediction")