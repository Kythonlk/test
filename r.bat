@echo off

if not "%~1"=="" (
  echo This script requires administrator privileges to run.
  exit /b 1
)

set "zip=C:\Program Files\WinRAR\rar.exe"  ** (Double-check this path)**
set "backupFolder=D:\test\backup"
set "logFile=D:\test\archive_log.txt"

del "%logFile%" >nul 2>&1

set "folder=D:\test\ac"
set "archiveFileName=ac.rar"
:ArchiveFolder
setlocal enabledelayedexpansion

if not exist "!folder!" (
  echo Folder "!folder!" does not exist. Skipping... >> "!logFile!"
  goto End
)

echo Checking if WinRAR exists at "%zip%" >> "!logFile!"
if not exist "%zip%" (
  echo WinRAR executable not found at "%zip%". Check the path. >> "!logFile!"
  goto End
)

%zip% a -r "!backupFolder!\!archiveFileName!" "!folder!" >> "!logFile!" 2>&1

if errorlevel 1 (
  echo Error archiving "!folder!": Check WinRAR path or folder permissions  >> "!logFile!"
) else (
  %zip% t "!backupFolder!\!archiveFileName!" >> "!logFile!" 2>&1
  if errorlevel 1 (
    echo Error testing archive "!backupFolder!\!archiveFileName!": Archive is corrupt or unreadable. >> "!logFile!"
  ) else (
    echo Folder "!folder!" archived and tested successfully. >> "!logFile!"
    echo Moving archive to backup folder >> "!logFile!"
    move "!backupFolder!\!archiveFileName!" "!backupFolder!\!archiveFileName!" >> "!logFile!" 2>&1
    if errorlevel 1 (
      echo Error moving archive "!backupFolder!\!archiveFileName!" to "!backupFolder!": Check folder permissions. >> "!logFile!"
    ) else (
      echo Archive "!archiveFileName!" moved successfully to "!backupFolder!". >> "!logFile!"
    )
  )
)

endlocal
:End

echo Attempting to archive folder... >> "!logFile!"
echo Script execution complete. Check "%logFile%" for details. >> "!logFile!"

:: Start your startup apps
start "" "C:\Path\To\Your\ysab.exe"
start "" "C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
start "" "C:\Path\To\Your\Terminal.exe"
