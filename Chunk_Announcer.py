import socket
import os
import math

serverPort = 12000

# Create a UDP socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
serverSocket.bind( ('', serverPort) )
print("The server is ready to receive")

while 1:
	message, clientAddress = serverSocket.recvfrom(2048)
	print('received {} bytes from {}'.format(len(message), clientAddress))
	modifiedMessage = message
	serverSocket.sendto(modifiedMessage, clientAddress)

	content_name = message.decode("utf-8")
	filename = content_name+'.txt'
	c = os.path.getsize(filename)
	print(c)
	CHUNK_SIZE = math.ceil(math.ceil(c)/5) 
	print(CHUNK_SIZE)

	index = 1
	with open(filename, 'rb') as infile:
		chunk = infile.read(int(CHUNK_SIZE))
		while chunk:
			chunkname = content_name+'_'+str(index)+'.txt'
			print("chunk name is: " + chunkname + "\n")
			with open(chunkname,'wb+') as chunk_file:
				chunk_file.write(chunk)
				index += 1
				chunk = infile.read(int(CHUNK_SIZE))
				chunk_file.close()

	chunknames = [content_name+'_1'+'.txt', content_name+'_2'+'.txt', content_name+'_3'+'.txt', content_name+'_4'+'.txt', content_name+'_5'+'.txt']

	with open('Client.txt', 'wb') as outfile:
            for chunk in chunknames: 
		           with open(chunk, 'rb') as infile: 
			            outfile.write(infile.read() )
		           infile.close() 
		           print(chunk + " chunk is saved!" +"\n")