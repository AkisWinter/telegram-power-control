#!/usr/bin/bash
# Create virtual environment and install dependencies

# Change to script directory
cd "$(dirname "$0")"

# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
source .venv/bin/activate

# Install required packages
pip install -r requirements.txt