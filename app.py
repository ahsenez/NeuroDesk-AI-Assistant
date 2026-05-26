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
