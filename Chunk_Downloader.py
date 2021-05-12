import socket


serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence = input('Input lowercase sentence:')
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print(modifiedSentence.decode())
clientSocket.close()

if (decodedMessage in chunks):
        req_ip = chunks[decodedMessage]
    else:
        print("peer yok")
