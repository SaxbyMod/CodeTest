import os
import random
from PIL import Image

# Set base path
base_path = "Art"

def random_image_from_folder(folder_path):
    """Returns a random image path from a given folder."""
    images = [f for f in os.listdir(folder_path) if f.endswith(('.png', '.jpg', '.jpeg'))]
    return os.path.join(folder_path, random.choice(images))

def generate_portrait():
    # Choose a random subfolder option
    subfolder_options = [f.path for f in os.scandir(base_path) if f.is_dir()]
    
    # Diagnostic prints:
    print("Subfolder options:", subfolder_options)
    
    chosen_option = random.choice(subfolder_options)
    
    # Diagnostic prints:
    print("Chosen option:", chosen_option)

    # Collect one random image from each of its sub-subfolders
    sub_subfolders = [f.path for f in os.scandir(chosen_option) if f.is_dir()]
    images = [random_image_from_folder(sub_subfolder) for sub_subfolder in sub_subfolders]

    # Diagnostic prints:
    print("Selected images:", images)

    # Combine the images by overlaying (stacking)
    base_img = Image.open(images[0])

    for img_path in images[1:]:
        img = Image.open(img_path)
        base_img = Image.alpha_composite(base_img, img)

    # Save the result
    base_img.save('combined_portrait.png')
    base_img.show()

generate_portrait()

random.seed(None)  # Use current system time