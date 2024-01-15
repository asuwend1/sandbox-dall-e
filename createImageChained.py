import os
import openai
import aiohttp
import asyncio
import secret
import time

openai.api_key = secret.api_key

# Set the prompts
prompts = ["robot dog in a lab", "robot dog exploring the city", "robot dog watching the sunset"]

async def fetch_and_save_image(session, url, path):
    try:
        async with session.get(url) as resp:
            img_data = await resp.read()
            with open(path, 'wb') as handler:
                handler.write(img_data)
    except Exception as e:
        print(f"Unexpected error: {e}")

async def fetch_image(prompt, i):
    try:
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="256x256"
        )

        # Get the image URL from the response
        image_url = response['data'][0]['url']

        # Download and save the image
        async with aiohttp.ClientSession() as session:
            await fetch_and_save_image(session, image_url, f"robot_dog_journey_{i+1}.jpg")
    except openai.api_errors.APIError as e:
        # This will catch any error returned by the OpenAI API
        print(f"API error: {e}")

    except Exception as e:
        # This is a catch-all for any other exceptions
        print(f"Unexpected error: {e}")

async def main():
    start_time = time.time()  # Start measuring execution time

    tasks = []
    for i, prompt in enumerate(prompts):
        tasks.append(fetch_image(prompt, i))

    await asyncio.gather(*tasks)

    end_time = time.time()  # End measuring execution time
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time} seconds")

# Run the main function
asyncio.run(main())