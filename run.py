from src import create_app
from flask import current_app
import os

app = create_app()

if __name__ == "__main__":
    with app.app_context():
        upload_folder = current_app.config['UPLOAD_FOLDER']
        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)
            print(f"Создана папка для загрузок: {upload_folder}")
        
        print(f"Сервер запущен. Папка хранения: {upload_folder}")
        print(f"Доступ по адресу: http://localhost:5000")
    
    app.run(host='0.0.0.0', port=5000, debug=True)