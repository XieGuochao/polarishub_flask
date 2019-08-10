import socket

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