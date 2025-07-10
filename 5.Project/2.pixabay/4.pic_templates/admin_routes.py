from flask import Blueprint, render_template, redirect, request, url_for
import os 
from file_data import file_keywords

UPLOAD_FOLDER = 'uploads'

admin_bp = Blueprint('admin', __name__)



@admin_bp.route('/', methods=['GET'])

def uploaded_file():
    files = os.listdir(UPLOAD_FOLDER)
    return render_template('admin.html', files=files, keywords = file_keywords)


@admin_bp.route('/', methods=['POST'])
def upload_file():
    file = request.files['file']
    filepath = os.path.join('./', UPLOAD_FOLDER, file.filename)
    file.save(filepath)
    return redirect(url_for('admin.uploaded_file'))


@admin_bp.route('/keyword', methods=['POST'])
def add_keyword():
    filename = request.form.get('filename')
    keyword = request.form.get('keyword')
    
    if filename in file_keywords:
        file_keywords[filename].append(keyword)
    else:
        file_keywords[filename] = [keyword]

    return redirect(url_for('admin.uploaded_file'))


