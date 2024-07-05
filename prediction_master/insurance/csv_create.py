# Author : Technource
# Date & Time : 2024/07/05 18:27
# Insurance CSV trained CSV file
import random # For get random values from the list, range,...etc
import csv # For csv file operations
path = "./prediction_master/insurance/"
# Generate trained CSV with random data of age and gender
with open(f'{path}insurance.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    # CSV Headers
    field = ["age", "gender", "will_buy"]
    writer.writerow(field)
    # Lets create upto 300 random records
    for x in range(1, 301):
        age = random.randint(18,100) # Random age between 18 to 100
        gender = random.randint(1,2) # Random gender 1: Male | 2: Female
        will_buy = random.randint(1,2) # Random value for 1: Will buy | 2: Will not buy
        writer.writerow([age, gender, will_buy]) # CSV row creation