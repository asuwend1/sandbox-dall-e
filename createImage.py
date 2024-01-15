import os
import openai
import secret
from PIL import Image, ImageOps
from io import BytesIO
import requests

openai.api_key = secret.api_key

# Generate the base image
def generate_base_image(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="512x512"
    )
    return response['data'][0]['url']

base_image_url = generate_base_image('red apple')

img_data = requests.get(base_image_url).content
with open('image_name.jpg', 'wb') as handler:
    handler.write(img_data)