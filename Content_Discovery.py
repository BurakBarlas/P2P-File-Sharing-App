import socket
import json

# 2.2.0-A
serverPort = 15200

# Create a UDP socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
serverSocket.bind(('', serverPort))
print("The server is ready to receive")

chunks = {}

while 1:
    message, clientAddress = serverSocket.recvfrom(2048)
    print('received {} bytes from {}'.format(len(message), clientAddress))
    print('"{}" : {}'.format(clientAddress, message.decode("utf-8")))

    # 2.2.0-B

    decodedMessage = message.decode("utf-8")
    if (decodedMessage in chunks):
        chunks[decodedMessage].append(clientAddress[0])
    else:
        chunks[decodedMessage] = [clientAddress[0]]

    f = open("Content_Dictionary.txt", "w")
    json.dump(chunks, f)
    f.close()


serverSocket.close()
