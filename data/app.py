from flask import Flask, request, jsonify
import pandas as pd
from rasa.core.agent import Agent
from rasa.core.interpreter import RasaNLUInterpreter

app = Flask(__name__)

# Load Rasa agent for processing user input
interpreter = RasaNLUInterpreter("models/nlu")
agent = Agent.load("models/dialogue", interpreter=interpreter)

df = None

@app.route('/')
def home():
    return "Welcome to the Conversational Data Analysis Bot!"

# Endpoint to upload CSV and process data
@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    global df
    df = pd.read_csv(file)
    return jsonify({"message": "CSV uploaded successfully. You can now ask questions!"})

# Endpoint to interact with the bot
@app.route('/ask', methods=['POST'])
def ask():
    if df is None:
        return jsonify({"error": "No data uploaded. Please upload a CSV file first."})

    user_input = request.json['message']
    response = process_query(user_input)
    return jsonify({"response": response})

def process_query(user_input):
    # Process the query with Rasa
    responses = agent.handle_text(user_input)
    return responses[0]['text']

if __name__ == '__main__':
    app.run(debug=True)
