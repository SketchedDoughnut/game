# Import socket module 
import socket     

port = 12345 
host = socket.gethostname() 

# create local server, client-side
messenger = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                  
 
# connect to the server
messenger.connect(('192.168.68.131', 12345))
 
# receive data from the server and decoding to get the string.
print(messenger.recv(1024).decode('utf-8'))

# close the connection 
messenger.close()