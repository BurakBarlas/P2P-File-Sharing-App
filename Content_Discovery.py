import socket

serverIP = 'localhost'
serverPort = 12000
server_address = (serverIP, serverPort)

# Create a UDP socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = input('Input file name :')

clientSocket.sendto(message.encode("utf-8"),server_address)

modifiedMessage, server = clientSocket.recvfrom(2048)
print(modifiedMessage.decode("utf-8"))

clientSocket.close()