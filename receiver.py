import socket
import time

TCP_PORT = 9999
UDP_PORT = 9999
BUFFER_SIZE = 1024

def tcp_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', TCP_PORT))
    s.listen(1)
    conn, addr = s.accept()
    print(f"TCP connection from {addr}")
    start = time.time()
    while True:
        data = conn.recv(BUFFER_SIZE)
        if not data:
            break
    end = time.time()
    print(f"TCP transfer complete in {end - start:.2f} seconds")
    conn.close()

def udp_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('', UDP_PORT))
    print("Waiting for UDP packets...")
    start = time.time()
    while True:
        data, addr = s.recvfrom(BUFFER_SIZE)
        if data == b'end':
            break
    end = time.time()
    print(f"UDP transfer complete in {end - start:.2f} seconds")

protocol = input("Enter protocol (tcp/udp): ").strip().lower()
if protocol == 'tcp':
    tcp_server()
elif protocol == 'udp':
    udp_server()
else:
    print("Invalid protocol")

