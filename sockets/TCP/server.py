import socket
import commons

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('', commons.SERVER_PORT))
serverSocket.listen(1)

while True:
    conn, addr = serverSocket.accept()
    print(f"connected to {addr}")
    with conn:
        data = conn.recv(1024)
        if not data: break
        conn.sendall(data) # echo
