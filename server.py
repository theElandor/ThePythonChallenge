import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
    print("Waiting for connection...")
    clientsocket, adress = s.accept()
    print("Connection from"+str(adress)+" has been established.")
    clientsocket.send(bytes("Welcome to the server!", "utf-8"))
