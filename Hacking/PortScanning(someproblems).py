##networking hacking
import socket
import subprocess
import sys
from datetime import datetime
import errno


remoteServer = input("Enter a remote host to scan: ")
remoteServerIP = socket.gethostbyname(str(remoteServer))
print("Please wait , scanning " + remoteServer)
t1 = datetime.now()
try:
    for port in range(1,1025):
        sock = socket.socket()
        result = sock.connect_ex((remoteServerIP,port))
        if result == 0:
            print("Port: "+str(port) + ": Open")
        else:
            print("Port: "+str(port) + ": Closed")
        sock.close()

except KeyboardInterrupt:
    sys.exit()
except socket.gaierror:
    sys.exit()
except socket.error:
    sys.exit()

t2 = datetime.now()
total = t2-t1
print("Scanning completed in "+str(total) +" seconds")



