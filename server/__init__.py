import os
import sys
sys.path.insert(0, os.getcwd())
print(sys.path)
from flask import Flask, request, abort, send_file, render_template

import server.network as server
import server.file_handler as file_handler
import server.myqrcode as myqrcode
import json

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True, static_url_path='/static')
    app.config.from_mapping(
        SECRET_KEY='dev',
        # DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    @app.route('/')
    def main():
        if network.checkIP(request.remote_addr):
            # From Host
            return "From Host"
        else:
            # From client
            return "From Client"

    @app.route('/files/', defaults = {"filename":""})
    @app.route('/files/<path:filename>', methods=['GET', 'POST'])
    def file(filename):
        print("files/" + filename)
        local_path = os.path.join(os.getcwd(), 'files', filename)
        print (local_path)
        is_admin = network.checkIP(request.remote_addr)

        if os.path.isfile(local_path):
            return send_file(local_path)
        elif os.path.isdir(local_path):
            return render_template('index.html', cwd = local_path, dirs = file_handler.get_dir(local_path), is_admin = is_admin)
        else:
            abort(404)

    @app.route('/opendir')
    def opendir():
        if network.checkIP(request.remote_addr):
            local_path = request.values.get('dir')
            print(local_path)
            os.system("nautilus {}".format(local_path))
            return "Success"
        else:
            return abort(404)

    @app.route('/settings')
    def open_setting():
        if network.checkIP(request.remote_addr):
            return render_template("settings.html")
        else:
            return abort(404)

    @app.route('/qr')
    def qr():
        filepath = request.values.get("filepath")
        print(filepath, hash(filepath))
        file_name = filepath + "_" + str(hash(filepath)) + ".png"
        print(file_name)
        return myqrcode.generateCode(filepath, file_name)

    return app