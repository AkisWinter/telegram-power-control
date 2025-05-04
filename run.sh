#!/bin/bash
# Activate virtual environment and run the Telegram bot

# Navigate to the script directory
cd "$(dirname "$0")"

# Activate virtual environment
source .venv/bin/activate

# Run the bot
python main.py