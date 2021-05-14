import socket
import json

serverIP = 'localhost'
serverPort = 8000
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

req_message = input('Name of the File:')

chunknames = [req_message+'_1',
              req_message+'_2', req_message+'_3',
              req_message+'_4', req_message+'_5']

temp_chunks_json = {"requested_content":  chunknames[0]}

with open('Content_Dictionary.txt','r') as infile:
    all_message = infile.read()
    
    temp_eval = eval(all_message)
    json_dump = json.dumps(temp_eval)
    json_object = json.loads(json_dump)
    
    print(json_object[chunknames[0]][0])
    
    clientSocket.connect((json_object[chunknames[0]][0], serverPort))
    clientSocket.send(str(temp_chunks_json).encode())
    
    modifiedSentence = clientSocket.recv(1024)
    
    print(modifiedSentence.decode("utf-8"))
infile.close()



# if (decodedMessage in chunks):
#        req_ip = chunks[decodedMessage]
# else:
#        print("peer yok")


clientSocket.close()