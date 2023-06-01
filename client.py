import socket
import time

# Function to send data of a specific size
def send_data(data_size):
    s = socket.socket()
    
    # Server IP address and port
    ip = '127.0.0.1'
    port = 8801
    
    # Number of requests to send
    num_requests = 1000
    
    s.connect((ip, port))
    rtt_times = []  # RTT times for each request
    print("Connected")
    
    # Prepare the data based on the desired size
    data = bytes(1) * data_size
    
    for _ in range(num_requests):
        # Start time of sending the message
        start_time = time.time()
        
        # Send the data to the server
        s.send(data)
        
        # Receive a response from the server
        s.recv(1024)
        
        # End time of receiving the response
        end_time = time.time()
        
        # Calculate the RTT
        rtt = end_time - start_time
        rtt_times.append(rtt)
    
    # Close the connection
    s.close()
    
    # Calculate the average RTT
    avg_rtt = sum(rtt_times) / num_requests
    
    print("Average RTT: ", avg_rtt)

# Menu for selecting data size
def print_menu():
    print("Select the data size:")
    print("1. 1 Byte")
    print("2. 1 KB")
    print("3. 2 KB")
    print("4. 4 KB")
    print("5. 8 KB")
    print("6. 16 KB")
    print("0. Exit")

# Handle user's choice
def handle_choice(choice):
    if choice == 0:
        print("Exiting the program...")
        return False
    elif choice == 1:
        send_data(1)  # 1 Byte
    elif choice == 2:
        send_data(1024)  # 1 KB
    elif choice == 3:
        send_data(2 * 1024)  # 2 KB
    elif choice == 4:
        send_data(4 * 1024)  # 4 KB
    elif choice == 5:
        send_data(8 * 1024)  # 8 KB
    elif choice == 6:
        send_data(16 * 1024)  # 16 KB
    else:
        print("Invalid choice. Please try again.")
    
    return True

# Main program loop
def main():
    while True:
        print_menu()
        choice = int(input("Enter your choice: "))
        
        if not handle_choice(choice):
            break

# Run the main program
if __name__ == "__main__":
    main()
