# Author : Technource
# Date & Time : 2024/07/05 19:27
# Music CSV trained CSV file
import random # For get random values from the list, range,...etc
import csv # For csv file operations
path = "./prediction_master/music/"
# Music basic categories
categories = ["HipHop", "Jazz", "Bass", "Rock", "Classic"]
# Generate trained CSV with random data of categories, age and gender
with open(f'{path}music.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    # CSV Headers
    field = ["age", "gender", "music"]
    writer.writerow(field)
    # Lets create upto 300 random records
    for x in range(1, 301):
        age = random.randint(18,100) # Random age between 18 to 100
        gender = random.randint(1,2) # Random gender 1: Male | 2: Female
        music = random.choice(categories) # Random category from the categories list
        writer.writerow([age, gender, music]) # CSV row creation