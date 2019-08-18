from MyQR import myqr
import os

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
    return qr_name
# print(version, level, qr_name)