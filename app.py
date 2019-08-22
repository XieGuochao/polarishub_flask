import server, os
from multiprocessing import Process

app = server.create_app()
def open_browser():
    if os.name == 'nt':
        os.system("start http://localhost:5000/")
    else:
        os.system("python -m webbrowser \"http://localhost:5000/\"")

def start_app():
    app.run(host="0.0.0.0", port=5000)

if __name__ == "__main__":
    open_browser()
    start_app()