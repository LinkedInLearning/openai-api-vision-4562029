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
                    "text": 'My refrigirator should have. Milk, Cheese, fruits, vigetable and chocolate pudding. What\'s missing? response should be a list of items that are missing ["missing item1", "missing item2", "missing item3", "missing item4", "missing item5"]',
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://media.istockphoto.com/id/508701233/photo/filled-refrigerator.jpg?s=1024x1024&w=is&k=20&c=OUosdX_9OFPtKQN8Nxkxf5L5Ur_hiusf6CS3O6FlYjg=",
                    },
                },
            ],
        }
    ],
    max_tokens=300,
)

print(response.choices[0])
import ipdb

ipdb.set_trace()
