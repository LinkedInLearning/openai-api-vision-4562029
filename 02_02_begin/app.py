import base64
import json
from io import BytesIO

from flask import Flask, jsonify, render_template, request
from openai import OpenAI

app = Flask(__name__)

client = OpenAI()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/vision", methods=["POST"])
def vision():
    """api endpoint"""
    if "file" not in request.files:
        return "No file part in the request", 400
    file = request.files["file"]
    prompt = ""
    file_content = file.read()
    # core logic
    return jsonify(["item1", "item2", "item3"])


if __name__ == "__main__":
    app.run(debug=True)
