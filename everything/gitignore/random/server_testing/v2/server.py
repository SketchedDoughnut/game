# first, make the recieving end
import socket


def listening_init():
    msg = 'Connection to server established.'.encode('utf-8')
    in_client.send(msg)
    print('Message sent!')


port = 12345  
#host = socket.gethostname()

# set up local server
local_server = socket.socket()  
local_server.bind(('', port))

# set up out client
#out_client = socket.socket()
#out_client.connect(host, port)

# set up in client
print('Listening for a connection...')
local_server.listen(50)
in_client, addr = local_server.accept()
local_server.close()
print('Got connection from', addr)

listening_init()
local_server.close()
in_client.close()