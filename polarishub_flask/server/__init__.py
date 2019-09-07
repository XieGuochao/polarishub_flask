import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from polarishub_flask.server.parser import printv

# printv(sys.path)
from flask import Flask, request, abort, send_file, render_template, redirect, url_for

from polarishub_flask.server import network as server
from polarishub_flask.server import file_handler as file_handler
from polarishub_flask.server import myqrcode as myqrcode
import json
from polarishub_flask.server import help

os_name = os.name
platform = sys.platform
# printv("os_name:", os_name)
printv ("platform:", platform)
printv ("cwd:", os.getcwd())

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
            return redirect("/files/")
        else:
            # From client
            return redirect("/files/")            

    @app.route('/files/', defaults = {"filename":""})
    @app.route('/files/<path:filename>', methods=['GET', 'POST'])
    def file(filename):
        printv("files/" + filename)
        local_path = os.path.join(os.getcwd(), 'files', filename)
        if platform=="win32":
            local_path = local_path.replace("/", "\\")
        printv (local_path)
        is_admin = network.checkIP(request.remote_addr)

        if os.path.isfile(local_path):
            return send_file(local_path)
        elif os.path.isdir(local_path):
            return render_template('index.html', cwd = local_path.replace('\\', "\\\\") if platform=="win32" else local_path, 
                                   dirs = file_handler.get_dir(local_path), is_admin = is_admin, 
                                   user_settings = file_handler.get_settings(), ip = network.get_host_ip())
        else:
            abort(404)

    @app.route('/opendir')
    def opendir():
        if network.checkIP(request.remote_addr):
            local_path = request.values.get('dir')
            printv(local_path)
            if platform == "win32":
                os.system("explorer {}".format(local_path))
            elif platform == "darwin":
                os.system("open {}".format(local_path))
            else:
                os.system("nautilus {}".format(local_path))
            return "Success"
        else:
            return abort(403)

    @app.route('/settings')
    def open_setting():
        if network.checkIP(request.remote_addr):
            return render_template("settings.html", user_settings = file_handler.get_settings())
        else:
            return abort(403)

    @app.route('/temp/<path:temppath>')
    def temp(temppath):
        file_path = os.path.join(os.getcwd(), 'temp', temppath)
        return send_file(file_path)

    @app.route('/qr', methods = ['POST'])
    def qr():
        file_path = request.form["filepath"]
        # file_path = request.form.get('filepath')
        printv(file_path, hash(file_path))
        file_name = str(hash(file_path)) + ".png"
        printv(file_name)
        network_path = "http://{}:{}".format(network.get_host_ip(), request.host[request.host.find(":")+1:]) + file_path
        printv("network_path", network_path)
        return render_template("qrcode.html", filepath=myqrcode.generateCode(network_path, file_name)[1], filename=file_path, user_settings = file_handler.get_settings())

    @app.route("/about")
    def about():
        return redirect('/static/about.html')
        # return render_template("about.html")
    
    @app.route('/update_settings', methods = ["POST"])
    def update_settings():
        if network.checkIP(request.remote_addr):
            if file_handler.update_settings(request.form):
                return redirect("/")
            else:
                return abort(500)
        else:
            return abort(403)

    @app.route('/halt')
    def halt():
        if network.checkIP(request.remote_addr):
            printv("Halting")
            func = request.environ.get('werkzeug.server.shutdown')
            if func is None:
                raise RuntimeError('Not running with the Werkzeug Server')
            func()
            return "PolarisHub shutting down..."
        else:
            return abort(403)
    
    @app.route('/help')
    def help_page():
        return redirect('/static/help.html')
        # return render_template('help.html', help_content = help.help_content)

    return app