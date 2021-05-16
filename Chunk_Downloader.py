import socket
import json

serverIP = 'localhost'
serverPort = 8000
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

req_message = input('Name of file to download : ')

chunknames = [req_message+'_1',
              req_message+'_2', req_message+'_3',
              req_message+'_4', req_message+'_5']

Successful_Download = True
i = 0
j = 0
z = 0
while i < 5:
    with open('Content_Dictionary.txt','r') as infile:
        all_message = infile.read()
    
        temp_eval = eval(all_message)
        json_dump = json.dumps(temp_eval)
        json_object = json.loads(json_dump)
    
        
        temp_chunks_json = {"requested_content":  chunknames[i]}
        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientSocket.connect((json_object[chunknames[i]][j], serverPort))
        clientSocket.send(str(temp_chunks_json).encode())
    
        recieved_message = clientSocket.recv(1024)
        chunk_info = recieved_message.decode("utf-8")
        
        with open(chunknames[i] + '.png', 'wb') as outfile:
            outfile.write(chunk_info)
        
        outfile.close()
        
        clientSocket.close()
        
        try:
            with open(chunknames[i] + '.png' , 'r') as test_success:
                
                test_success.close()
                Successful_Download = True
        except:
            Successful_Download = False
            
        if Successful_Download == True :
            print(json_object[chunknames[i]][j] , ' : ' , chunknames[i] + " ( Successful )")
        else:
            print(json_object[chunknames[i]][j] , ' : ' , chunknames[i] + " ( Retrying from another peer )")
            
            if j <= len(json_object[chunknames[i]])-1:
                j += 1
                if j < len(json_object[chunknames[i]]):
                    i -= 1
                else:
                    j = 0
                    print('CHUNK "' + chunknames[i] + '" CANNOT BE DOWNLOADED FROM ONLINE PEERS')
                  
    i += 1
    infile.close()



try:
    with open('Forest' + '.png', 'wb') as outfile:
    	for chunk in chunknames: 
		    with open(chunk + '.png', 'rb') as infile: 
			    outfile.write(infile.read() )
		    infile.close()
    print("Download successful.")
    
except:
    print("The chunks of the file to be download are not complete.")