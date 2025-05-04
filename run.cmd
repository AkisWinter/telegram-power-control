@echo off
REM Activate virtual environment and run the Telegram bot

REM Change to your project directory
cd /d %~dp0

REM Activate virtual environment
call .venv\\Scripts\\activate.bat

REM Run the bot
python main.py

pause
