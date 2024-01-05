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
    item_list = json.loads(request.form.get("userItems", "[]"))
    if not item_list:
        return jsonify(
            ["Please enter items that are supposed to be in the refrigerator"]
        )
    prompt = f""""""
    print(prompt)
    file_content = file.read()
    base64_image = base64.b64encode(file_content).decode("utf-8")


if __name__ == "__main__":
    app.run(debug=True)
