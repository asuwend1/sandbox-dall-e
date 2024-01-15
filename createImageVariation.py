import os
import openai
import secret
import requests
openai.api_key=secret.api_key

response = openai.Image.create_variation(
  image=open("image_name.png", "rb"),
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']
#using the url, we use the code below to save it as a file
img_data = requests.get(image_url).content
with open('image_name_var.png', 'wb') as handler:
    handler.write(img_data)