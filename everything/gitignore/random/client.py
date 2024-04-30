# Import socket module 
import socket             
 
# Create a socket object 
s = socket.socket()         
 
# Define the port on which you want to connect 
port = 12345               
 
# connect to the server on local computer 
#s.connect(('127.0.0.1', port)) 
#s.connect(('192.168.68.1', port))
host = socket.gethostname()
s.connect((host, port))
 
# receive data from the server and decoding to get the string.
#print(s.recv(1024).decode())
import base64
print(base64.b64decode(s.recv(1024)))

# close the connection 
s.close()     