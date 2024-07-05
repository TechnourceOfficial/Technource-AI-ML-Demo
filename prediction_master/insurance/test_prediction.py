# Author : Technource
# Date & Time : 2024/07/05 20:27
# Insurance CSV trained CSV file
import joblib # For load trained insurance file
path = "./prediction_master/insurance/"
# Load trained Insurance model
model = joblib.load(f'{path}model.joblib')
# Predict model with Male with 33 age
will_buy = model.predict([[33,1]])
if will_buy and will_buy[0]:
    will_buy_label = "will buy"
    if will_buy[0] == 2:
        will_buy_label = "will not buy"
    print(f"Prediction for Male with age 33 {will_buy_label} insurance")
else:
    print("Something went wrong with the prediction")