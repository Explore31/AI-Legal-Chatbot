from flask import Flask, render_template, request
import requests
import google.generativeai as genai
import pandas as pd
import csv
import hashlib
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "0340d9058c3b6762658b67815b8f256f048a3713c083f8e07b8026c2efcd58fd"  # Needed for session management run the session.py to generate the session management seceret key from your local machine

# Configure GenerativeAI API key
genai.configure(api_key="AIzaSyCF_2eM5dqvDbDjndazATvTJNilGyTVPnY") #Your Api Key

def load_legal_data_from_csv(filename):
    legal_data = []
    with open(filename, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            legal_data.append(row[0])  # Assuming the legal information is in the first column (index 0)
    return legal_data

# Function to generate legal response using Gemini
def get_legal_response(user_query, relevant_legal_info):
    prompt = [
        "You are an expert in Indian law. Analyze the following scenario and provide a legal overview:\n\n",
        f"{relevant_legal_info}\n\n",
        f"User question: {user_query}",
    ]
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    return response.text

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

def find_relevant_legal_info(description, legal_data):
    keywords = description.lower().split()
    matching_info = []
    for entry in legal_data:
        entry_text = entry.lower()
        # Match all keywords (strict)
        if all(keyword in entry_text for keyword in keywords):
            matching_info.append(entry)
    # You can alternatively implement logic for partial matches here
    return matching_info

filename = "C:/Users/barat/Downloads/sample_workchatbot1/legalAI/static/ipc_sections.csv"
legal_data = load_legal_data_from_csv(filename)

# Helper function to hash passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Helper function to check hashed password
def verify_password(hashed_password, password):
    return hashed_password == hashlib.sha256(password.encode()).hexdigest()

# Existing routes (no changes needed)
@app.route("/")
def index():
    return render_template("index.html")

@app.route('/chatbot', methods=['GET', 'POST'])
def chatbot():
    if request.method == 'POST':
        description = request.form['description']
        relevant_legal_info = find_relevant_legal_info(description, legal_data)
        response = get_legal_response(description, relevant_legal_info)
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':  # Check if the request is an AJAX request
            return response  # Return only the response text
        else:
            return render_template('chatbot.html', response=response, description=description)
    return render_template('chatbot.html', response=None, description=None)


if __name__ == "__main__":
    app.run(debug=True)
