import socket
import json

# 2.2.0-A
serverPort = 5001

# Create a UDP socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
serverSocket.bind(('', serverPort))
print("The server is ready to receive")


contentDictionary = {
    "chunks": []
}

with open('contentDictionary.txt', 'w') as outfile:
    json.dump(contentDictionary, outfile)


while 1:
    message, clientAddress = serverSocket.recvfrom(2048)
    print('received {} bytes from {}'.format(len(message), clientAddress))

    # 2.2.0-B
    

    f = open("contentDictionary.txt", "w")
    f.write(str(contentDictionary))
    
    
    json.dump(contentDictionary, f)
    contentDictionary["chunks"].push(str(clientAddress))

    f.close()
    print('"{}" : {}'.format(clientAddress, message))
