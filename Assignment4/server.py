import socket

class Server:
	def __init__(self, bind_address='', port=4444):
		self.tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.tcp_sock.bind((bind_address, port))
	
	def start(self):
		self.tcp_sock.listen(5)
		while True:
			(cs, addr) = self.tcp_sock.accept()
			data = cs.recv(1024)
			data = data.decode() # expectd to recieve a string
			print("recieved message: " + str(data))
	
if __name__ == '__main__':
	s = Server()
	print("started server")
	s.start()
