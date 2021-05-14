import socket
import json

serverPort = 8000
serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print('The server is ready to receive')


while 1:
    connectionSocket, addr = serverSocket.accept()
    
    sentence = connectionSocket.recv(1024)
    
    decoded_message = sentence.decode()
    
    temp_eval = eval(decoded_message)
    json_dump = json.dumps(temp_eval)
    json_object = json.loads(json_dump)
    
    sending_item = json_object['requested_content']
    
    connectionSocket.send(sending_item.encode("utf-8"))
    
    connectionSocket.close()