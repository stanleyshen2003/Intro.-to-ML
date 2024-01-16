#!/bin/bash

# Assuming you're currently in the directory containing the 200 folders
# Replace 'source_directory' with the path to your main folder

source_directory="bird_data/train"
destination_directory="bird_data/test"

# Create the new folder if it doesn't exist
mkdir -p "$destination_directory"

# Loop through each folder in the source directory
for folder in "$source_directory"/*; do
    if [ -d "$folder" ]; then
        folder_name=$(basename "$folder")
        # Create a folder with the same name in the destination directory
        mkdir -p "$destination_directory/$folder_name"

        # Move 2 images from the current folder to the new folder
        counter=0
        for image in "$folder"/*; do
            if [ -f "$image" ] && [ "$counter" -lt 2 ]; then
                mv "$image" "$destination_directory/$folder_name/"
                ((counter++))
            fi
        done
    fi
done