from socket import *

serverIP = 'localhost'
serverPort = 12000
server_address = (serverIP, serverPort)

# Create a UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

message = input('Input lowercase sentence:')

clientSocket.sendto(message.encode("utf-8"),server_address)

modifiedMessage, server = clientSocket.recvfrom(2048)
print(modifiedMessage.decode("utf-8"))

clientSocket.close()