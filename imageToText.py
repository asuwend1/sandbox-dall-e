import os
import openai
from PIL import Image,ImageOps
from io import BytesIO
import requests
import secret

# Set API key and prompt
openai.api_key = secret.key

# WRITE YOUR CODE HERE
# Generate the base image
response = openai.Image.create(
    prompt="cute kitten playing with a ball of yarn",
    n=1,
    size="512x512"
)

image_url = response['data'][0]['url']

img_data = requests.get(image_url).content
with open('kitten.jpg', 'wb') as handler:
    handler.write(img_data)

# Generate a description with GPT-3
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=f"Describe the following image: [img]{image_url}[/img]",
    max_tokens=50,
    n=1,
    stop=None,
    temperature=0.7,
)

image_description = response.choices[0].text.strip()
print(image_description)