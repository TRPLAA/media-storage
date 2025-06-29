from . import app  # Относительный импорт
import os
import mimetypes
from flask import render_template, request, send_from_directory, send_file
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'mp4', 'mov', 'pdf', 'mp3', 'txt'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('index.html', files=files)

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'Файл не выбран', 400
        
    file = request.files['file']
    if file.filename == '':
        return 'Файл не выбран', 400
        
    if file and allowed_file(file.filename):
        # Обезопасим имя файла
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return '', 204
    else:
        return 'Недопустимый тип файла', 400
        

@app.route('/download/<filename>')
def download(filename):
    return send_from_directory(
        app.config['UPLOAD_FOLDER'],
        filename,
        as_attachment=True
    )

import magic

# Добавляем новый эндпоинт для превью
@app.route('/preview/<filename>')
def preview(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    mime = magic.Magic(mime=True)
    file_type = mime.from_file(file_path)
    
    # Для текстовых файлов
    if file_type.startswith('text/'):
        with open(file_path, 'r') as f:
            content = f.read()
        return f'<pre>{content}</pre>'
    
    return send_file(file_path)

@app.route('/delete/<filename>', methods=['DELETE'])
def delete_file(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if os.path.exists(file_path):
        os.remove(file_path)
        return '', 204
    return 'Файл не найден', 404

from PIL import Image
import io

@app.route('/thumbnail/<filename>')
def thumbnail(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    
    # Создаем миниатюру
    img = Image.open(file_path)
    img.thumbnail((200, 200))
    
    # Сохраняем в буфер
    img_io = io.BytesIO()
    img.save(img_io, 'JPEG')
    img_io.seek(0)
    
    return send_file(img_io, mimetype='image/jpeg')

# Запрещаем выполнение файлов
@app.before_request
def block_executables():
    if request.path.startswith('/preview/') or request.path.startswith('/download/'):
        filename = request.path.split('/')[-1]
        if filename.lower().endswith(('.exe', '.bat', '.sh', '.php')):
            return "Файлы этого типа запрещены", 403
# Кэширование миниатюр
from functools import lru_cache

@lru_cache(maxsize=100)
def generate_thumbnail(path, size=(200, 200)):
    img = Image.open(path)
    img.thumbnail(size)
    # ... сохранение в буфер ...