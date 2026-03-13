import socket
import threading
import os
from tqdm import tqdm
import pyfiglet
from termcolor import colored

print(colored(pyfiglet.figlet_format('UDP OPEN PORTS CHECKER VERSION 1\n\nSCRIPT MADE BY KRAINIUM\n\nDONT USE VPN TO RUN SCRIPT', font='term'), 'green'))


target_ip = input(colored(pyfiglet.figlet_format("Enter the target IP address: ", font='term'), 'blue'))
print(" ")
start_port = 1
end_port = 65536


if not os.path.exists('opened-ports'):
    os.mkdir('opened-ports')


def check_port(port):
    try:
        
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        s.settimeout(1)
        
        s.sendto(b"\x05\x9b\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x07\x65\x78\x61\x6d\x70\x6c\x65\x02\x63\x6f\x6d\x00\x00\x01\x00\x01", (target_ip, port))
        
        data, addr = s.recvfrom(1024)
        
        with open('opened-ports/open.txt', 'a') as f:
            if port == start_port:
                f.write(f"Target-IP: {target_ip}\n\n")
            f.write(f"Port {port} is opened!\n")
        print(colored(pyfiglet.figlet_format(f"\nPort {port} is open", font='term'), 'red'))
    except:
        
        pass
    finally:
        
        s.close()


def port_scan():
    
    threads = []
    
    for port in tqdm(range(start_port, end_port+1), desc="Scanning", unit="ports"):
        
        t = threading.Thread(target=check_port, args=(port,))
        
        threads.append(t)
        
        t.start()

    
    for t in threads:
        t.join()

    
    print(colored(pyfiglet.figlet_format("Port scan complete", font='term'), 'blue'))


port_scan()
