from src import app  # Изменён импорт
import os

if __name__ == "__main__":
    upload_folder = app.config['UPLOAD_FOLDER']
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)
        print(f"Создана папка для загрузок: {upload_folder}")
    
    print(f"Сервер запущен. Папка хранения: {upload_folder}")
    print(f"Доступ по адресу: http://localhost:5000")
    app.run(host='0.0.0.0', port=5000, debug=True)