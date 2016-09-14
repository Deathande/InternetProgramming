import socket

SERVER = '127.0.0.1'
PORT = 4444

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((SERVER, PORT))
s.sendall("E1.0 -945xx 1689 -950 230 -25 1".encode())
s.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((SERVER, PORT))
s.sendall("S0 2 -945 1689 -950 230 -25 1 1e-15".encode())
s.close()
