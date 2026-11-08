@echo off
chcp 65001 >nul
cd /d "%~dp0"
if "%~1"=="" (
  echo 請把圖片或資料夾拖到這個檔案上。
  pause
  exit /b
)
python img2webp.py %*
echo.
pause
