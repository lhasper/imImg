import pandas as pd
import requests
from PIL import Image
from io import BytesIO
import os

# Define the path to the CSV file
csv_file_path = 'C:\\Cont\\Python Projects\\BarcodeImage\\image1.csv'

# Define the directory to save the images
image_dir = 'C:\\Cont\\Python Projects\\BarcodeImage'
os.makedirs(image_dir, exist_ok=True)

# Load the CSV file
df = pd.read_csv(csv_file_path)

# Function to download and save an image
def download_and_convert_image(url, image_path):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for request errors
        image = Image.open(BytesIO(response.content))
        image = image.resize((175, 175))  # Resize image
        image.save(image_path, 'WEBP')  # Save image as WEBP
        print(f"Saved {image_path}")
    except Exception as e:
        print(f"Failed to process {url}: {str(e)}")

# Process each image URL in the DataFrame
for index, row in df.iterrows():
    image_url = row['Image']  # Adjust the column name based on your CSV
    file_name = f"{row['NewFileName']}.webp"  # Use the NewFileName column for the file name
    image_path = os.path.join(image_dir, file_name)
    download_and_convert_image(image_url, image_path)

print("All images processed.")
