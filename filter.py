import os
import openai
import secret
from PIL import Image
from io import BytesIO
import requests
from PIL import ImageFilter

openai.api_key = secret.api_key


# Generate the base image
def generate_base_image(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="512x512"
    )
    return response['data'][0]['url']

"""
base_image_url = generate_base_image('red apple')

img_data = requests.get(base_image_url).content
with open('base_apple.jpg', 'wb') as handler:
    handler.write(img_data)
"""
apple_image=Image.open('base_apple.jpg')

# Apply a Gaussian blur filter to the base image
blurred_image = apple_image.filter(ImageFilter.GaussianBlur(radius=5))

# Save the blurred image to a file
blurred_image.save('blurred_red_apple.jpg')

# Apply a contour filter to the base image
contour_image = apple_image.filter(ImageFilter.CONTOUR)

# Save the contour image to a file
contour_image.save('contour_red_apple.jpg')

# Apply an edge enhance filter to the base image
edge_enhanced_image = apple_image.filter(ImageFilter.EDGE_ENHANCE)

# Save the edge enhanced image to a file
edge_enhanced_image.save('edge_enhanced_red_apple.jpg')


# Apply a find edges filter to the base image
edge_image = apple_image.filter(ImageFilter.FIND_EDGES)

# Save the edge image to a file
edge_image.save('edge_red_apple.jpg')

