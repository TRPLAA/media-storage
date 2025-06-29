@echo off
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
set "drive=%drive%:\MediaStorage"

mkdir "%drive%" 2>nul
if not exist "%drive%" (
    echo Ошибка создания папки! Проверьте правильность ввода.
    goto disk_selection
)

echo Создание конфигурации...
echo { "storage_path": "%drive%" } > config/settings.json

echo Запуск сервера...
start "" run.py
echo Готово! Откройте: http://localhost:5000
pause