import socket
import os
import math
from time import time, sleep
import json

serverIP = 'localhost'
serverPort = 15200
server_address = (serverIP, serverPort)

# Create a UDP socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Calculates size of chunks

content_name = 'Server';
filename = content_name+'.png'
c = os.path.getsize(filename)
#print(c)
CHUNK_SIZE = math.ceil(math.ceil(c)/5) 
#print(CHUNK_SIZE)


#Seperates the file to chunks
index = 1
with open(filename, 'rb') as infile:
	chunk = infile.read(int(CHUNK_SIZE))
	while chunk:
		chunkname = content_name+'_'+str(index)+'.png'
		print("chunk name is: " + chunkname + "\n")
		with open(chunkname,'wb+') as chunk_file:
			chunk_file.write(chunk)
			index += 1
			chunk = infile.read(int(CHUNK_SIZE))
			chunk_file.close()

chunknames = [content_name+'_1',
              content_name+'_2', content_name+'_3',
              content_name+'_4', content_name+'_5']

chunk_set = {"chunks": [chunknames[0],chunknames[1],chunknames[2],chunknames[3],chunknames[4]]}


#print(chunk_set['chunks'])
with open('Announced_Chunks.txt','r') as infile:
    for line in infile:
        for word in line.split():
            chunk_set['chunks'].append(word)
infile.close()
#print(chunk_set['chunks'])

json_dump = json.dumps(chunk_set)
json_object = json.loads(json_dump)


#print(str(json_object))
        
# Broadcasts all chunks every 60 seconds

clientSocket.sendto(str(json_object).encode("utf-8"), server_address)
#while True:
#    sleep(60 - time() % 60)
#    while i<5:
#        temp_chunk_message = json_object["chunks"][i]
#        clientSocket.sendto(temp_chunk_message.encode("utf-8"), server_address)
#        modifiedMessage, server = clientSocket.recvfrom(2048)
#        print(modifiedMessage.decode("utf-8"))
#        i += 1
#    i = 0


    
    
        
        
clientSocket.close()
