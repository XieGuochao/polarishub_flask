# from MyQR import myqr
import qrcode
import os
from polarishub_flask.server.parser import printv

# def generateCode(url, filename = "qrcode.png"):
#     version, level, qr_name = myqr.run(
#         url,
#         version = 1,
#         level = 'H',
#         picture = None,
#         colorized = False,
#         contrast = 1.0,
#         brightness = 1.0,
#         save_name = filename,
#         save_dir = os.path.join(os.getcwd(), 'temp')
#     )
#     printv(qr_name)
#     return qr_name, '/' + qr_name[qr_name.find("temp"):].replace("\\", "/")

def generateCode(url, filename = "qrcode.png"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    qr_name = os.path.join(os.getcwd(), 'temp', filename)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(qr_name)
    printv(qr_name)
    return qr_name, '/' + qr_name[qr_name.find("temp"):].replace("\\", "/")