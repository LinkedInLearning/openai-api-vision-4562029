from io import BytesIO
import base64

from flask import Flask, render_template, jsonify, request
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

    file_content = file.read()
    base64_image = base64.b64encode(file_content).decode("utf-8")
    """
    use base64 encoding for images
     f"data:image/jpeg;base64,{base64_image}"
    """

    response = client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}",
                        },
                    }
                ],
            }
        ],
        max_tokens=300,
    )
    choice = response.choices[0].message.content
    return jsonify(choice)
    


if __name__ == "__main__":
    app.run(debug=True)
