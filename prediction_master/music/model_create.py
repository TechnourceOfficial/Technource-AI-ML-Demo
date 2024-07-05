# Author : Technource
# Date & Time : 2024/07/05 19:47
# Music trained model creation from the generated trained CSV
import pandas as pd # For read CSV file
from sklearn.tree import DecisionTreeClassifier # For train model
import joblib # For create prediction model
path = "./prediction_master/music/"
# Read music trained CSV file
music_data = pd.read_csv(f"{path}music.csv")
# Set age and gender as the input data
X = music_data.drop(columns=['music'])
# Set music category as result data
y = music_data['music']
# Create model
model = DecisionTreeClassifier()
# Train model with values and result
model.fit(X.values,y)
# Create a model for direct use
joblib.dump(model,f'{path}model.joblib')