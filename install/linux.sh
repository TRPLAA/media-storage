#!/bin/bash
echo "Установка Media Storage..."
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
mkdir -p uploads
echo "Запуск сервера в фоне..."
nohup python run.py > server.log &
echo "Готово! Откройте: http://$(hostname -I | cut -d' ' -f1):5000"