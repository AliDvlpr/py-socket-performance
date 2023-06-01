import socket
s = socket.socket()

# IP & Port config
ip = '127.0.0.1'
port = 8801

# Socket
s.bind((ip, port))
s.listen()
print("CONNECTED SUCSSEFULLY")
# Client Connection
c,addr = s.accept()

while True:
    # Receive messages from the client
    request = c.recv(1024)
    # Send a message to the client
    c.send(request)