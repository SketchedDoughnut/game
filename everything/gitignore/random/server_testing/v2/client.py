# Import socket module 
import socket     

port = 12345 
host = socket.gethostname() 

# create local server, client-side
messenger = socket.socket()                  
 
# connect to the server
messenger.connect((host, port))
 
# receive data from the server and decoding to get the string.
print(messenger.recv(1024).decode('utf-8'))

# close the connection 
messenger.close()