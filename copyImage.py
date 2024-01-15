import shutil

def copy_image(source_path, destination_path):
    try:
        shutil.copy2(source_path, destination_path)
        print("Image copied successfully!")
    except IOError as e:
        print(f"An error occurred while copying the image: {e}")

# Example usage
source_image = "original-copy.png"
destination_image = "original.png"
copy_image(source_image, destination_image)