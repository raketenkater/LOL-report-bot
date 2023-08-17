@echo off
rem This batch file assumes that the Python installer file, the requirements file and the Python file are in the same folder as this batch file.
rem Change the names of the files accordingly.

rem Check if Python is already installed
python --version >nul 2>&1
if %errorlevel% equ 0 (
    echo Python is already installed.
) else (
    rem Install Python using the installer file
    python3.9.exe /quiet InstallAllUsers=1 PrependPath=1
)

rem Install the required packages using the requirements file
pip install -r requirements.txt

if not exist mates mkdir mates

rem Run the Python file
python gui.py

rem Exit the batch file
exit
