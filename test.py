import socket

HELLO_MY_NAME_IS = socket.gethostname()
print(HELLO_MY_NAME_IS)
MY_IP = socket.gethostbyname(HELLO_MY_NAME_IS)
print(MY_IP)


with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.connect(('8.8.8.8', 53))
    MY_IP = s.getsockname()[1]
    print(MY_IP)
