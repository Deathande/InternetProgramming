import socket

# Developed with python 3, is backwards compatible with
# python 2

# Data
poly = [1, 2, 3, 4]
a = -2
b = 2
tol = 0.0001

# Server information
addr = '127.0.0.1'
port = 4444

s = None
# Constructs a valid message out of the given parameters
# to be sent to the server.
def construct_bisec_msg(a, b, poly, tol):
	poly_string = " ".join([str(x) for x in poly])
	arg_list = [a, b, poly_string, tol]
	arg = " ".join([str(x) for x in arg_list])
	# 'S' specifies bisection method
	return "S" + arg 

def construct_eval_msg(x, poly):
	poly_string = " ".join([str(x) for x in poly])
	# 'E' specifies evaluation
	return "E" + str(x) + " " + poly_string

def send_message(msg, addr, port):
	# s is pseudo global, it is initialized toward the beginning
	# of the file.
	# Note: this is not thread safe
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((addr, port))
	s.sendall(msg.encode())
	ret = s.recv(1024)
	s.close()
	return ret.decode()

def err(msg):
	print(msg)
	# s contains a socket in a pseudo global scope
	s.close()
	exit(1)

if __name__ == '__main__':
	msg = construct_bisec_msg(a, b, poly, tol)
	value = send_message(msg, addr, port)
	if value[0] == 'X':
		err(value)
	value = value[1:]
	print("The result of the bisection method is " + value)
	value = float(value)
	msg = construct_eval_msg(value, poly)
	value = send_message(msg, addr, port)
	if value[0] == 'X':
		err(value)
	value = float(value[1:])
	print("The result of the evaluation is: " + str(value))
	#print("The result of the 
