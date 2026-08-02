from flask import Flask, render_template, request, jsonify
from google import genai
from dotenv import load_dotenv
import os

# .env dosyasını yükle
load_dotenv()

app = Flask(__name__)

gemini_client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/command", methods=["POST"])
def command():
    data = request.get_json()

    user_message = data.get("command", "")

    try:
        response = client.responses.create(
            model="gpt-5.5",
            input=user_message
        )

        answer = response.output_text

        return jsonify({
            "response": answer
        })

    except Exception as e:
        return jsonify({
            "response": f"Error: {str(e)}"
        })


if __name__ == "__main__":
    app.run(debug=True)
