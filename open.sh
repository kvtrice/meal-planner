#!/bin/bash

# Prompt user for the filepath
read -p "Enter the name of the text file (e.g. "example.txt"): " file_path

# Check if the file exists
if [ ! -e "$file_path" ]; then
    echo "File not found: $file_path"
    echo "Please try again!"
    exit 1
fi

# Use the open command to open the file with default program
open "$file_path"