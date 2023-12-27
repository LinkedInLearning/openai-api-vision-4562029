import click
from openai import OpenAI

client = OpenAI()

PROMPT = """You are an e-commerce marketing expert. Here are some mugs. 
Create short, appealing descriptions for them for our e-commerce website. 
Output should only contain a JSON list of of strings containing descriptions.
"""

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
                        "url": "https://www.binaryville.com/images/products/fred-0s1s-mug-black.jpg",
                    },
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://www.binaryville.com/images/products/dolores-compute-mug-black.jpg",
                    },
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://www.binaryville.com/images/products/bubbles-gumball-mug-black.jpg",
                    },
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://www.binaryville.com/images/products/rex-microcontrollers-mug-black.jpg",
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
