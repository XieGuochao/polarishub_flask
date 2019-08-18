import os, sys, json
from flask import abort
settings = {}

def load_settings():
    with open(os.path.join(os.getcwd(), 'server', 'settings.json')) as f:
        return json.load(f)


def get_settings():
    global settings
    if settings == {} or settings is None:
        settings = load_settings()
    return settings

        
def get_dir(path):
    if os.path.isdir(path):
        return os.listdir(path)
    else:
        abort(404)