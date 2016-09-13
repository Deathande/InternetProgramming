import socket

SERVER = '127.0.0.1'
PORT = 4444

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((SERVER, PORT))
s.sendall("some message".encode())
