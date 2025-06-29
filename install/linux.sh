#!/bin/bash
echo "Установка Media Storage..."
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

echo
echo "Доступные разделы:"
df -h --output=target | grep -v 'Mounted'
echo
read -p "Введите путь для хранения файлов (например, /mnt/media): " storage_path

mkdir -p "$storage_path"
if [ $? -ne 0 ]; then
    echo "Ошибка создания папки! Проверьте права доступа."
    exit 1
fi

echo "Создание конфигурации..."
mkdir -p config
echo "{ \"storage_path\": \"$storage_path\" }" > config/settings.json

echo "Запуск сервера в фоне..."
nohup venv/bin/python run.py > server.log 2>&1 &

sleep 2
echo "Готово! Откройте: http://$(hostname -I | awk '{print $1}'):5000"
echo "Логи сервера: server.log"