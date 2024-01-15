import os
import openai
import secret
from PIL import Image, ImageOps
from io import BytesIO
import requests

openai.api_key = secret.api_key

# Manipulate the image properties
def manipulate_image(image, size, aspect_ratio, brightness, contrast, saturation, hue):
    # Resize the image
    new_size = (int(image.width * size), int(image.height * aspect_ratio * size))
    resized_image = image.resize(new_size, Image.ANTIALIAS)

    # Adjust the image properties
    from PIL import ImageEnhance, ImageOps
    enhanced_image = ImageEnhance.Brightness(resized_image).enhance(brightness)
    enhanced_image = ImageEnhance.Contrast(enhanced_image).enhance(contrast)
    enhanced_image = ImageEnhance.Color(enhanced_image).enhance(saturation)
    
    # Adjust hue using ImageOps module
    enhanced_image = ImageOps.colorize(enhanced_image.convert('L'), 'black', 'white', midpoint=128 - int(128 * hue))

    return enhanced_image

base_image = Image.open('image_name.jpg')
 # Example of image manipulation
manipulated_image = manipulate_image(
  base_image, size=0.5, aspect_ratio=1, brightness=1.2,
  contrast=1.5, saturation=0.8, hue=0.1
)
# Save the manipulated image to a file
manipulated_image.save('manipulated_red_apple.jpg')
