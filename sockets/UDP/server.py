import socket
import commons


serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind(("", commons.SERVER_PORT))
print(f"server listening at {commons.SERVER_PORT}")

while True:
    message, clientAddr = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode().upper()
    serverSocket.sendto(modifiedMessage.encode(), clientAddr)
    serverSocket.close()
    break
