from PIL import Image
import os

def save_image(image, user_id, base_dir):
    # Create the user-specific folder
    user_folder = os.path.join(base_dir, f"user_{user_id}")
    os.makedirs(user_folder, exist_ok=True)

    # Find the next available number for the file name
    existing_files = os.listdir(user_folder)
    numbers = [int(f.split('.')[0]) for f in existing_files if f.split('.')[0].isdigit()]
    next_number = max(numbers, default=0) + 1

    # Create the file path for saving
    file_path = os.path.join(user_folder, f"{next_number}.jpg")
    
    # Save the image to the specified path
    image.save(file_path)
    return file_path

# Input variables
image = Image.open(r"C:\Users\DISAL\OneDrive\Desktop\about_us_head.jpg")  # Use a raw string to handle backslashes
user_id = "x"
base_dir = r"C:\Users\DISAL\OneDrive\Desktop"  # Base directory

# Call the function
saved_path = save_image(image, user_id, base_dir)

print(f"Image saved at: {saved_path}")
