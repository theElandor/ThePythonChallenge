import socket
s = socket.socket()
IP = "localhost"
PORT = 1234
s.bind((IP, PORT))
s.listen(5)

print("Waiting for connection...")
clientsocket, adress = s.accept()
print("Connection from"+str(adress)+" has been established.")
clientsocket.send(bytes("Welcome to the server!", "utf-8"))
data = []
while True:
    try:
        msg = clientsocket.recv(1024)
        if msg:
            print(msg.decode("utf-8"))
            data.append(msg.decode("utf-8"))
    except WindowsError:
        break
for element in data:
    print(element , end = "")