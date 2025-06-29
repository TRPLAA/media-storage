from flask import render_template, request, send_from_directory
from . import app
import os

@app.route('/')
def index():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('index.html', files=files)

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file:
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    return '', 204

@app.route('/download/<filename>')
def download(filename):
    return send_from_directory(
        app.config['UPLOAD_FOLDER'],
        filename,
        as_attachment=True
    )