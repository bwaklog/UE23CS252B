import socket

import commons

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((commons.SERVER_NAME, commons.SERVER_PORT))
    s.sendall(b'Hello')
    data = s.recv(1024)
    print(f"recieved {repr(data)}")
