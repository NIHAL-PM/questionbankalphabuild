import json
import os
import random
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Directory where questions are stored
QUESTIONS_FOLDER = os.path.join(os.getcwd(), "questions_folder")

# Load questions from JSON files
def load_questions():
    questions = []
    for filename in os.listdir(QUESTIONS_FOLDER):
        if filename.endswith(".json"):
            file_path = os.path.join(QUESTIONS_FOLDER, filename)
            with open(file_path, "r") as f:
                batch = json.load(f)
                questions.extend(batch)
    return questions

# Cache questions on startup
all_questions = load_questions()

# Route for the main page
@app.route('/')
def index():
    return render_template('index.html')

# API endpoint to get a random question
@app.route('/get_question', methods=['GET'])
def get_question():
    if not all_questions:
        return jsonify({"error": "No questions available"}), 404
    question = random.choice(all_questions)
    return jsonify(question)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)