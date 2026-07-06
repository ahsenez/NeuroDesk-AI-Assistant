from flask import Flask, render_template, request, jsonify
from datetime import datetime
import webbrowser

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/command", methods=["POST"])
def command():
    data = request.get_json()
    user_command = data.get("command", "").lower()

    if "time" in user_command:
        response = f"The current time is {datetime.now().strftime('%H:%M')}."
    elif "date" in user_command:
        response = f"Today's date is {datetime.now().strftime('%d %B %Y')}."
    elif "youtube" in user_command:
        response = "Opening YouTube..."
    elif "google" in user_command:
        response = "Opening Google..."
    elif "task" in user_command:
        response = "Task added to your productivity list."
    elif "hello" in user_command:
        response = "Hello, I am NeuroDesk AI. How can I assist you today?"
    else:
        response = "Command analyzed. NeuroDesk AI is ready to assist you."

    return jsonify({"response": response})

