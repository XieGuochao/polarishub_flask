from MyQR import myqr
import os
from polarishub_flask.server.parser import printv

def generateCode(url, filename = "qrcode.png"):
    version, level, qr_name = myqr.run(
        url,
        version = 1,
        level = 'H',
        picture = None,
        colorized = False,
        contrast = 1.0,
        brightness = 1.0,
        save_name = filename,
        save_dir = os.path.join(os.getcwd(), 'temp')
    )
    printv(qr_name)
    return qr_name, '/' + qr_name[qr_name.find("temp"):].replace("\\", "/")
# printv(version, level, qr_name)