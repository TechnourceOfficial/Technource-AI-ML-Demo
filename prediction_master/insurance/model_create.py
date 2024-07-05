# Author : Technource
# Date & Time : 2024/07/05 19:47
# Insurance trained model creation from the generated trained CSV
import pandas as pd # For read CSV file
from sklearn.tree import DecisionTreeClassifier # For train model
import joblib # For create prediction model
path = "./prediction_master/insurance/"
# Read insurance trained CSV file
insurance_data = pd.read_csv(f"{path}insurance.csv")
# Set age and gender as the input data
X = insurance_data.drop(columns=['will_buy'])
# Set insurance category as result data
y = insurance_data['will_buy']
# Create model
model = DecisionTreeClassifier()
# Train model with values and result
model.fit(X.values,y)
# Create a model for direct use
joblib.dump(model,f'{path}model.joblib')