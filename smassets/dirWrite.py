import os
import csv

# Define the directory path
directory_path = r'C:\Cont\Python Projects\BarcodeImage'

# Define the CSV file path where the results will be saved
csv_file_path = 'file_names.csv'

# Create a list to store file names
file_names = []

# Traverse through the directory
for file_name in os.listdir(directory_path):
    # Full path of the current file
    file_path = os.path.join(directory_path, file_name)
    # Check if it's a file and not a directory
    if os.path.isfile(file_path):
        # Check if the file name is exactly 16 characters long
        if len(file_name) == 16:
            new_file_name = '0' + file_name
            new_file_path = os.path.join(directory_path, new_file_name)
            os.rename(file_path, new_file_path)  # Rename the file
            file_name = new_file_name  # Update file_name variable to new name for CSV
        file_names.append([file_name])

# Write the file names to a CSV file
with open(csv_file_path, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Write a header row
    writer.writerow(['File Name'])
    # Write file names
    writer.writerows(file_names)

print(f"File names have been written to {csv_file_path}")
