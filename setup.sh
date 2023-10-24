#!/bin/bash

# Create a virtual environment
python3 -m venv .venv

# Activate the virtual environment
source .venv/bin/activate

# Install project dependencies
pip install -r requirements.txt

# Run the main.py script
python3 main.py
