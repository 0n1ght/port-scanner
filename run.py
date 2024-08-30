import socket

def scan(target, num_ports):
    for port in range(1, num_ports + 1):
        scan_port(target, port)

def scan_port(ip_address, port):
    try:
        sock = socket.socket()
        sock.connect((ip_address, port))
        print("[+] Port {} Opened".format(port))
        sock.close()
    except Exception as e:
        print("[-] Port {} Closed".format(port))

for i in range(49650, 50000):
    scan_port("192.168.100.168", i)
