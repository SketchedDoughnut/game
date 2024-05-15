import socket

host = "192.168.68.121"
#host = "73.67.252.89"
port = 9999
#port = 0

def send_data(msg):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(msg.encode())
        data = s.recv(1024)
        print('data:', data)

send_data('test!')