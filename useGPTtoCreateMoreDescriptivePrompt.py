import os
import openai
from PIL import Image,ImageOps
from io import BytesIO
import secret

# Set API key and prompt
openai.api_key = secret.key

user_input = "Create an image of a car"

# Generate more descriptive text with GPT-3
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=f"Create a more descriptive scene based on this user input: '{user_input}'.",
    max_tokens=50,
    n=1,
    stop=None,
    temperature=0.7,
)

descriptive_text = response.choices[0].text.strip()
print(descriptive_text)
#descriptive_text = "The car is a sleek, silver convertible with bright red leather seats. It's parked in front of a beautiful mansion with a fountain in the middle."

# Generate the base image
response = openai.Image.create(
    prompt=descriptive_text,
    n=1,
    size="512x512"
)

image_url = response['data'][0]['url']

img_data = requests.get(image_url).content
with open('base_img.jpg', 'wb') as handler:
    handler.write(img_data)