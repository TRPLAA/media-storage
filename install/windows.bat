@echo off
echo Установка Media Storage...
python -m venv venv
call venv\Scripts\activate
pip install -r requirements.txt
mkdir uploads
echo Запуск сервера...
start "" run.py
echo Готово! Откройте в браузере: http://localhost:5000
pause