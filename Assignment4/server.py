import polynomials
import socket
import re

class Server:
	def __init__(self, bind_address='', port=4444):
		self.tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.tcp_sock.bind((bind_address, port))
	
	def start(self):
		self.tcp_sock.listen(5)
		while True:
			(cs, addr) = self.tcp_sock.accept()
			print("Client connected from " + str(addr[0]))
			data = cs.recv(1024)
			data = data.decode() # expected to receive a string
			try:
				ci = ClientInput(data)
				if ci.t == 'E':
					print("Client requesting evaluation")
					ans = polynomials.evaluate(ci.arg1, ci.arguments)
				if ci.t == 'S':
					print("Client requesting bisection")
					ans = polynomials.bisection(ci.arg1, ci.arg2, ci.arguments, ci.tol)
					#print (ans)
			except Exception:
				print("Client sent invalid data")
	
class ClientInput:
	def __init__(self, client_string):
		self.arguments = re.split("\s+", client_string)
		arg1 = self.arguments.pop(0)
		if arg1[0] == 'E':
			self.t = 'E'
			self.arg1 = float(arg1[1:])
		elif arg1[0] == 'S':
			self.t = 'S'
			self.arg1 = float(arg1[1:])
			self.arg2 = float(self.arguments.pop(0))
			self.tol = float(self.arguments.pop())
		else:
			raise Exception('Invalid command from client')
		self.arguments = [float (x) for x in self.arguments]
	
if __name__ == '__main__':
	try:
		s = Server()
		print("started server")
		s.start()
	except KeyboardInterrupt:
		print("Shutting down")
		s.tcp_sock.close()
	else:
		s.tcp_sock.close()

