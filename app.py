from flask import Flask, render_template, request, jsonify
from datetime import datetime
import webbrowser

app = Flask(__name__)
