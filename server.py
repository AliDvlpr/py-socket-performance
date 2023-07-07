import socket
import threading

# IP & Port config
ip = '127.0.0.1'
port = 8801

# Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ip, port))
s.listen()
print("Server started. Waiting for connections...")


def handle_client(client_socket):
    while True:
        # Receive messages from the client
        request = client_socket.recv(16384)
        
        if not request:
            break
        
        # Send the received data back to the client
        client_socket.send(request)
    
    # Close the client connection
    client_socket.close()


while True:
    # Accept a client connection
    client_socket, addr = s.accept()
    print("Connected to client:", addr)
    
    # Start a new thread to handle the client connection
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()