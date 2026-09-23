import os
import shutil

# Ask the user for the folder path
source_folder = input("Enter the folder path: ")

# Create the destination folder
destination_folder = os.path.join(source_folder, "JPG_Files")

if not os.path.exists(destination_folder):
    os.mkdir(destination_folder)

# Check all files in the source folder
for filename in os.listdir(source_folder):

    # Check if the file is a JPG image
    if filename.lower().endswith(".jpg"):
        source_file = os.path.join(source_folder, filename)
        destination_file = os.path.join(destination_folder, filename)

        # Move the JPG file
        shutil.move(source_file, destination_file)

print("All JPG files have been moved successfully!")
