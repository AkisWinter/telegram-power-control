@echo off
REM Create virtual environment and install dependencies

REM Change to script directory
cd /d %~dp0

REM Create virtual environment
python -m venv .venv

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Install required packages
pip install -r requirements.txt

pause