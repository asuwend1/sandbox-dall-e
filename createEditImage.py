import os
import openai
import secret
import requests
openai.api_key=secret.api_key
# Keep CODE ABOVE
# WRITE YOUR CODE HERE


response=openai.Image.create_edit(
  image=open("original-copy.png", "rb"),
  mask=open("masked.png", "rb"),
  prompt="a vibrant modern office with red chairs and a television screen.a snack is on the table. ",
  n=1,
  size="512x512"
)
image_url = response['data'][0]['url']
#using the url, we use the code below to save it as a file
img_data = requests.get(image_url).content
with open('edited.png', 'wb') as handler:
    handler.write(img_data)