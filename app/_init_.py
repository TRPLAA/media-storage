from flask import Flask

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 2000 * 1024 * 1024 * 1024  # 2000GB лимит

from app import routes