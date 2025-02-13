import socket
import commons

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
message = input("input msg(will be translated to lowercase): ").lower()

clientSocket.sendto(message.encode(), (commons.SERVER_NAME, commons.SERVER_PORT))
modifiedMessage, serverAddr = clientSocket.recvfrom(2048)

print(f"recv: {modifiedMessage.decode()}")
clientSocket.close()
