import socket
import threading
import os
from tqdm import tqdm
import pyfiglet
from termcolor import colored

print(colored(pyfiglet.figlet_format('UDP OPEN PORTS CHECKER VERSION 1\n\nSCRIPT MADE BY KRAINIUM\n\nDONT USE VPN TO RUN SCRIPT', font='term'), 'green'))

# Define the target IP address and port range
target_ip = input(colored(pyfiglet.figlet_format("Enter the target IP address: ", font='term'), 'blue'))
print(" ")
start_port = 1
end_port = 65536

# Create a folder to store the results
if not os.path.exists('opened-ports'):
    os.mkdir('opened-ports')

# Define a function to check if a UDP port is open using a DNS request
def check_port(port):
    try:
        # Create a UDP socket
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # Set a timeout of 1 second
        s.settimeout(1)
        # Send a DNS request to the target IP address on the specified port
        s.sendto(b"\x05\x9b\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x07\x65\x78\x61\x6d\x70\x6c\x65\x02\x63\x6f\x6d\x00\x00\x01\x00\x01", (target_ip, port))
        # Receive the response from the target
        data, addr = s.recvfrom(1024)
        # If no exception was raised, print the port number and save it to file
        with open('opened-ports/open.txt', 'a') as f:
            if port == start_port:
                f.write(f"Target-IP: {target_ip}\n\n")
            f.write(f"Port {port} is opened!\n")
        print(colored(pyfiglet.figlet_format(f"\nPort {port} is open", font='term'), 'red'))
    except:
        # If an exception was raised, the port is assumed to be closed
        pass
    finally:
        # Close the socket
        s.close()

# Define a function to run the UDP port scan using multiple threads
def port_scan():
    # Create a list of threads
    threads = []
    # Loop through the port range
    for port in tqdm(range(start_port, end_port+1), desc="Scanning", unit="ports"):
        # Create a new thread for each port
        t = threading.Thread(target=check_port, args=(port,))
        # Add the thread to the list
        threads.append(t)
        # Start the thread
        t.start()

    # Wait for all threads to complete
    for t in threads:
        t.join()

    # Print a message indicating the scan is complete
    print(colored(pyfiglet.figlet_format("Port scan complete", font='term'), 'blue'))

# Run the port scan function
port_scan()
