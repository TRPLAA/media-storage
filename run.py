from app import app
import os

if __name__ == "__main__":
    # Создать папку для загрузок, если её нет
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    
    app.run(host='0.0.0.0', port=5000)