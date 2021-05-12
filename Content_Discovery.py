import socket
import json

# 2.2.0-A
serverPort = 15200

# Create a UDP socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
serverSocket.bind(('', serverPort))
print("The server is ready to receive")


contentDictionary = {
    "chunks": []
}


while 1:
    message, clientAddress = serverSocket.recvfrom(2048)
    print('received {} bytes from {}'.format(len(message), clientAddress))
    print('"{}" : {}'.format(clientAddress, message.decode("utf-8")))
    
    
    # 2.2.0-B
    #contentDictionary = json.loads(message)
    contentDictionary["chunks"] = message.decode("utf-8")

    contentDictionary = json.loads(message)
    contentDictionary["chunks"].push(clientAddress)

    f = open("contentDictionary.txt", "w")
    json.dump(contentDictionary, f)
    f.close()

    
serverSocket.close()