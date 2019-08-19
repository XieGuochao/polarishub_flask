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
        path_list = os.listdir(path)
        # print (path_list, path)
        print(os.getcwd())
        path_list = [(path_list[i], os.path.isfile(os.path.join(path, path_list[i])), os.path.join(path[len(os.getcwd()):], path_list[i])) for i in range(len(path_list))]
        print ("path_list", path_list)
        return path_list
    else:
        abort(404)