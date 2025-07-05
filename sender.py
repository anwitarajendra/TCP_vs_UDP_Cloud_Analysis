import socket
import time

TCP_PORT = 9999
UDP_PORT = 9999
BUFFER_SIZE = 2048
NUM_PACKETS = 5000
RECEIVER_IP = '13.203.200.48'

def tcp_client():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((RECEIVER_IP, TCP_PORT))
    start = time.time()
    for _ in range(NUM_PACKETS):
        s.send(b'x' * BUFFER_SIZE)
    s.shutdown(socket.SHUT_WR)
    end = time.time()
    print(f"TCP send complete in {end - start:.2f} seconds")
    with open("results.txt", "a") as f:
        f.write(f"TCP {BUFFER_SIZE} {NUM_PACKETS} {end - start:.4f} seconds\n")
    s.close()


def udp_client():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    start = time.time()
    for _ in range(NUM_PACKETS):
        s.sendto(b'x' * BUFFER_SIZE, (RECEIVER_IP, UDP_PORT))
    s.sendto(b'end', (RECEIVER_IP, UDP_PORT))
    end = time.time()
    print(f"UDP send complete in {end - start:.2f} seconds")
    with open("results.txt", "a") as f:
        f.write(f"UDP {BUFFER_SIZE} {NUM_PACKETS} {end - start:.4f} seconds\n")


protocol = input("Enter protocol (tcp/udp): ").strip().lower()
if protocol == 'tcp':
    tcp_client()
elif protocol == 'udp':
    udp_client()
else:
    print("Invalid protocol")
