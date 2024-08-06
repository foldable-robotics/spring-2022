import socket

host = '192.168.4.199' # substitute your vinyl cutter's ip address
port = 8080                   # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.sendall(b'IN;U0,0;U1000,0;U1000,1000;@;')
s.close()