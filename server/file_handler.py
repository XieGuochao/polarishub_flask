import os, sys, json
settings = {}

def load_settings():
    with open(os.path.join(os.getcwd(), 'server', 'settings.json')) as f:
        return json.load(f)


def get_settings():
    global settings
    if settings == {} or settings is None:
        settings = load_settings()
    return settings