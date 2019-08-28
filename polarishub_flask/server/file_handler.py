import os, sys, json
from flask import abort
from polarishub_flask.server.parser import printv
settings = {}

def load_settings():
    with open(os.path.join(os.getcwd(), 'server', 'settings.json')) as f:
        return json.load(f)


def get_settings():
    global settings
    if settings == {} or settings is None:
        settings = load_settings()
    return settings

def save_settings():
    try:
        with open(os.path.join(os.getcwd(), 'server', 'settings.json'), 'w') as f:
            json.dump(settings, f)
        return True
    except:
        return False

def get_dir(path):
    if os.path.isdir(path):
        path_list = os.listdir(path)
        # printv (path_list, path)
        printv(os.getcwd())
        path_list = [(path_list[i], os.path.isfile(os.path.join(path, path_list[i])), os.path.join(path[len(os.getcwd()):], path_list[i])) for i in range(len(path_list))]
        printv ("path_list", path_list)
        return path_list
    else:
        abort(404)

keys = {
    'username': lambda name:len(name)>0
    } 
def update_settings(new_settings):
    global settings
    printv(new_settings)
    # for items in new_settings:
        # printv (items)
    for key, value in new_settings.items():
        # printv(items)
        # key, value = items
        printv ((key, value))
        if key in keys.keys() and keys[key](value):
            printv ("key gets:", key)
            printv (key, value)
            if value:
                settings[key] = value
        else:
            settings = load_settings()
            return False

    if save_settings():
        return True
    else:
        return False