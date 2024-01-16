#!/bin/bash
if [ -z "$2" ]; then
	echo "./merge_data.sh folder1 folder2"
	return 0
fi
# Define paths to the two big folders
folder1=$1
folder2=$2

# Loop through the subfolders in folder1
for subfolder1 in `ls "${folder1}"`; do
    # Extract the subfolder name from the path
    mv "${folder2}/${subfolder1}"/* "${1}/${subfolder1}"
done
rm -r "$2"

echo "Merge completed."
