# Import socket module 
import socket             
 
# Create a socket object 
s = socket.socket()         
 
# Define the port on which you want to connect 
port = 12345               
 
# connect to the server on local computer 
s.connect(('127.0.0.1', port)) 
 
# receive data from the server and decoding to get the string.
while True:
    #print(s.recv(1024).decode())
    import base64
    print(base64.b64decode(s.recv(1024)))

# close the connection 
s.close()     