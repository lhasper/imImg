import os
import requests
from PIL import Image
from io import BytesIO
import pandas as pd

# Function to download and save an image as .webp
def download_and_save_image(url, item_id, folder_path):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes

        image = Image.open(BytesIO(response.content))
        webp_path = os.path.join(folder_path, f"{item_id}.webp")
        image.save(webp_path, 'WEBP')

    except requests.RequestException as e:
        print(f"Request error for {item_id}: {e}")
    except IOError as e:
        print(f"Image error for {item_id}: {e}")

# Load the CSV file
csv_file_path = 'C:\Cont\ItemManager\itemwithurl.csv' # Replace with your CSV file path
data = pd.read_csv(csv_file_path)

# Folder where the images will be saved
folder_path = r'C:\Cont\ItemManager\images'
os.makedirs(folder_path, exist_ok=True)

# Process each row in the dataframe
for _, row in data.iterrows():
    download_and_save_image(row['url'], row['itemId'], folder_path)

print("Download process completed.")