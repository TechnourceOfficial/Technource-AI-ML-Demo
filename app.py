# Author : Technource
# Date & Time : 2024/07/05 22:00
# Flask application
# Load Flask framework
from flask import Flask, render_template, request, jsonify, make_response
# Load model dependency
import joblib
# JSON
import json
# OpenAI
from openai import OpenAI
# App initialization
app = Flask(__name__)
# Home Page
@app.route("/")
def index():
    return render_template("index.html")

# OpenAI request
def openAIRequest(prompt,api_key):
    try:
        client = OpenAI(
            # This is the default and can be omitted
            api_key=api_key,
        )
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="gpt-3.5-turbo"
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error: {e}")
        return "API Key is not valid OR key does not have balance"

# For get users details and predict on the data
@app.route("/get-predictions", methods=['POST'])
def getPredictions():
    # Users Details
    req_data = request.get_json()
    name = req_data['name']
    height = req_data['height']
    weight = req_data['weight']
    openai_key = req_data['openai_key']
    age = req_data['age']
    gender = req_data['gender']
    genderInfo = "Male" if gender == '1' else "Female"
    prompt = f"""
        Please create a diet plan for the user with following details. 
        please send only diet plan. No other information is required.
        User details is as below: User name is {name}. Height is {height} cm. Weight is {weight} kg.
        age is {age}. Gender is {genderInfo}.
    """
    ai_diet_plan = "N/A"

    if openai_key and openai_key != "":
        ai_diet_plan = openAIRequest(prompt,openai_key)
        
    # Default results
    predicted_music = "N/A"
    predicted_insurance = "N/A"

    # Load Music Trained Model
    music_model_path = "./prediction_master/music/"
    music_model = joblib.load(f'{music_model_path}model.joblib')
    fav_music = music_model.predict([[age,gender]])
    if fav_music and fav_music[0]:
        predicted_music = fav_music[0]
    
    # Load Insurance Trained Model
    insurance_model_path = "./prediction_master/insurance/"
    insurance_model = joblib.load(f'{insurance_model_path}model.joblib')
    will_buy = insurance_model.predict([[age,gender]])
    if will_buy and will_buy[0]:
        predicted_insurance = will_buy[0]
        predicted_insurance = int(predicted_insurance)

    # Result Object
    result = {
        'predicted_music' :predicted_music,
        'predicted_insurance' :predicted_insurance,
        'ai_diet_plan' :ai_diet_plan,
    }

    # Response
    response = {
        'data' : result,
        'status': 200
    }

    response = json.dumps(response)

    return response

if __name__ == '__main__':
    app.run()