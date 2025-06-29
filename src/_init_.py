import json
import os
from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Загрузка конфигурации
    config_path = os.path.join(os.path.dirname(__file__), '../config/settings.json')
    try:
        with open(config_path) as f:
            config = json.load(f)
            app.config['UPLOAD_FOLDER'] = config['storage_path']
    except Exception as e:
        print(f"Ошибка загрузки конфига: {e}")
        app.config['UPLOAD_FOLDER'] = os.path.abspath('uploads')
    
    app.config['MAX_CONTENT_LENGTH'] = 500 * 1024 * 1024
    return app

app = create_app()

# Импорт должен быть ПОСЛЕ создания app
from src import routes