# first of all import the socket library 
import socket             
 
# next create a socket object 
server = socket.socket()         
print ("Socket successfully created")
 
# reserve a port on your computer in our 
# case it is 12345 but it can be anything 
port = 12345               
 
# Next bind to the port 
# we have not typed any ip in the ip field 
# instead we have inputted an empty string 
# this makes the server listen to requests 
# coming from other computers on the network 
server.bind(('', port))         
print ("socket binded to %s" %(port)) 
 
# put the socket into listening mode 
server.listen(5)     
print ("socket is listening...")            
 
# a forever loop until we interrupt it or 
# an error occurs 
while True: 
 
    # Establish connection with client. 
    client, addr = server.accept()     
    print('Got connection from', addr )
 
    # send a thank you message to the client. encoding to send byte type. 
    #client.send('Thank you for connecting'.encode()) 
    import base64
    client.send(base64.b64encode(b'Thank your connecting!'))
 
    # Close the connection with the client 
    client.close()
   
    # Breaking once connection closed
    break

# https://stackoverflow.com/questions/12993276/errno-10061-no-connection-could-be-made-because-the-target-machine-actively-re
# https://stackoverflow.com/questions/55302927/what-ip-address-should-be-used-in-a-client-server-program