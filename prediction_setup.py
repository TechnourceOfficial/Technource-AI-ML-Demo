# Author : Technource
# Date & Time : 2024/07/05 20:00
# Create trained CSV files and model of Music and Insurance
import os
import time
print("Music Prediction Model Creation")
time.sleep(1)
print("Creating trained music CSV file with random data")
os.system("py prediction_master/music/csv_create.py")
time.sleep(1)
print("Music trained CSV file generated")
time.sleep(1)
print("Creating trained music model")
os.system("py prediction_master/music/model_create.py")
time.sleep(1)
print("Trained Music model generated")
time.sleep(1)
print("Test Music prediction")
os.system("py prediction_master/music/test_prediction.py")
time.sleep(1)
print("Insurance Prediction Model Creation")
time.sleep(1)
print("Creating trained insurance CSV file with random data")
os.system("py prediction_master/insurance/csv_create.py")
time.sleep(1)
print("Insurance trained CSV file generated")
time.sleep(1)
print("Creating trained insurance model")
os.system("py prediction_master/insurance/model_create.py")
time.sleep(1)
print("Trained Insurance model generated")
time.sleep(1)
print("Test Insurance prediction")
os.system("py prediction_master/insurance/test_prediction.py")