import click
from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4-vision-preview",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Here is a mug. Create an short, appealing description for it for an e-commerce website. Output should only contain text.",
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://binaryville.com/images/products/rex-microcontrollers-mug-black.jpg",
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
