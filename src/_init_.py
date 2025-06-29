import os
import json
from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Путь к конфигурации
    base_dir = os.path.abspath(os.path.dirname(__file__))
    config_path = os.path.join(base_dir, '..', 'config', 'settings.json')
    
    # Стандартная папка, если конфиг отсутствует
    default_upload = os.path.join(base_dir, '..', 'uploads')
    
    try:
        with open(config_path) as f:
            config = json.load(f)
            storage_path = config.get('storage_path', default_upload)
            # Нормализация пути
            app.config['UPLOAD_FOLDER'] = os.path.abspath(storage_path)
    except Exception as e:
        print(f"Ошибка загрузки конфига: {e}")
        app.config['UPLOAD_FOLDER'] = os.path.abspath(default_upload)
    
    app.config['MAX_CONTENT_LENGTH'] = 500 * 1024 * 1024
    
    # Регистрация маршрутов
    from .routes import bp
    app.register_blueprint(bp)
    
    return app