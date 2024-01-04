import base64
import click
from openai import OpenAI

client = OpenAI()


with open("refrigerator.png", "rb") as f:
    file_content = f.read()
    base64_image = base64.b64encode(file_content).decode("utf-8")

PROMPT = """"""

response = client.chat.completions.create(
    model="gpt-4-vision-preview",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": PROMPT,
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image}",
                    },
                },
            ],
        }
    ],
    max_tokens=300,
)
try:
    click.secho(response.choices[0].message.content, fg="cyan")
except:
    print(response.choices[0].message.content)
