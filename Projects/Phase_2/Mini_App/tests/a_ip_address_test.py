import socket

host = socket.gethostname()
name = socket.gethostbyname(host)
address = socket.gethostbyaddr(name)
def get_internet_ip():
    try:
        #obtains websocket by the given parameters
        #AF_INET obtains the IP v4 address
        #SOCK_DGRAM obtains the ucp port
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        s.connect(('8.8.8.8', 80))

        ip_address = s.getsockname()[0]
    except Exception:
        ip_address = 'Unable to determine'
    finally:
        s.close()
    return ip_address

local_ip = get_internet_ip()
print(f'Host name is {name}')
print(f'Address is {address}')
print(f'The local IP is {local_ip}')