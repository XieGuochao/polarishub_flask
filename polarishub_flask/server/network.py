import socket
from polarishub_flask.server.parser import printv

host_ip = None

def get_host_ip():
    global host_ip
    if host_ip is not None:
        return host_ip

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        host_ip = s.getsockname()[0]
    finally:
        s.close()

    return host_ip

def checkIP(addr):
    return addr == "127.0.0.1"
    # if 'HTTP_X_FORWARDED_FOR' in request.META :
    #     ip =  request.META['HTTP_X_FORWARDED_FOR']
    # else:
    #     ip = request.META['REMOTE_ADDR']
    # # printv("IP: ", ip)
    # return ip == "127.0.0.1"