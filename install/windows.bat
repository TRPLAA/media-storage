@echo off
chcp 65001 > nul
setlocal enabledelayedexpansion

echo Установка Media Storage...
python -m venv venv
call venv\Scripts\activate
pip install -r requirements.txt

:disk_selection
echo.
echo Доступные диски:
wmic logicaldisk get caption
echo.
set /p drive="Выберите диск для хранения файлов (например, D): "
set "drive=!drive!:\MediaStorage"

mkdir "!drive!" 2>nul
if not exist "!drive!" (
    echo Ошибка создания папки! Проверьте правильность ввода.
    goto disk_selection
)

echo Создание конфигурации...
mkdir config 2>nul
echo { "storage_path": "!drive!" } > config\settings.json

echo Запуск сервера...
start "" venv\Scripts\python run.py
echo.
echo ================================================
echo Готово! Откройте в браузере: http://localhost:5000
echo.
echo Если сервер не запустился автоматически, выполните:
echo   cd %~dp0
echo   venv\Scripts\python run.py
echo ================================================
pause