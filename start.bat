@echo off

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    REM Install Python from website
    echo Python is not installed, installing now...
    REM Replace the URL below with the appropriate Python installer URL for your platform
    curl -O https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe
    REM Replace the installer filename below with the appropriate filename for your platform
    start /wait "" python-3.10.0-amd64.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
    REM Remove the installer file
    del python-3.10.0-amd64.exe
)

REM Install required packages
echo Installing required packages...
pip install -r requirements.txt

REM Start Django development server
echo Starting Django development server...
start python manage.py runserver 192.168.1.102:8000
