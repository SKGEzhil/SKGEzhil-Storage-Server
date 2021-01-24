# main.py

import os
from datetime import datetime
import flask_login
from flask import *
from flask_login import login_required, current_user
from . import db
from .models import Files

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/uploader', methods=['GET', 'POST'])
@login_required
def upload_file():
    date = datetime.today().strftime('%y-%m-%d')
    time = datetime.today().strftime('%H:%M:%S')
    print(date)
    print(time)
    if request.method == 'POST':
        f = request.files.getlist('file')
        for file in f:
            file.save(
                os.path.join(f'/home/skgezhil/Workspace/storage_server/storage/{flask_login.current_user}',
                             file.filename))
            new_file = Files(user_id=f'{flask_login.current_user}', date=f'{date}', time=f'{time}',
                             file_name=f'{file.filename}')
            db.session.add(new_file)
            db.session.commit()
        return render_template('uploader.html')


@main.route('/myphotos', defaults={'req_path': ''})
@main.route('/myphotos/<path:req_path>')
def photo_viewer(req_path):
    print(flask_login.current_user)
    base_dir = f'/home/skgezhil/Workspace/storage_server/storage/{flask_login.current_user}'

    abs_path = os.path.join(base_dir, req_path)

    if request.path != '/':
        print("ok")
    else:
        print("no")

    if not os.path.exists(abs_path):
        return abort(404)

    if os.path.isfile(abs_path):
        return send_file(abs_path)

    files = os.listdir(abs_path)
    return render_template('files.html', files=files)


@main.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

@main.route('/upload')
@login_required
def upload():
    print(flask_login.current_user)
    isdir = os.path.isdir(f'/home/skgezhil/Workspace/storage_server/storage/{flask_login.current_user}')
    if not isdir:
        os.makedirs(f'/home/skgezhil/Workspace/storage_server/storage/{flask_login.current_user}')
    return render_template('upload.html', name=current_user.name)
