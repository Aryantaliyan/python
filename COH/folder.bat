@echo off
set /p count=Enter the chapter number:
set "folderName=chapter%count%"
mkdir "%folderName%"
echo Folder "%folderName%" has been created.
pause
