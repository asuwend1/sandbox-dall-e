import os
import openai
import secret
import requests
openai.api_key=secret.api_key

response = openai.Image.create(
  prompt="a cat climbing a tree.",
  n=3,
  size="256x256"
)

image_url = response['data']
#print(image_url)

image_url1 = response['data'][0]['url']
image_url2 = response['data'][1]['url']
image_url3  = response['data'][2]['url']

#print(image_url1)

img_data = requests.get(image_url1).content
with open('image_name1.jpg', 'wb') as handler:
    handler.write(img_data)
img_data = requests.get(image_url2).content
with open('image_name2.jpg', 'wb') as handler:
    handler.write(img_data)
img_data = requests.get(image_url3).content
with open('image_name3.jpg', 'wb') as handler:
    handler.write(img_data)