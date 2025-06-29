from app import app
import os

if __name__ == "__main__":
    # Создать папку для загрузок, если её нет
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    
    # Запустить на всех IP в локальной сети
    app.run(host='0.0.0.0', port=5000)