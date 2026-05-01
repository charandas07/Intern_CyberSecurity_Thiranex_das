import socket

target = input("Enter target: ")
ports = [21,22,23,80,443]

for port in ports:
    sock = socket.socket()
    sock.settimeout(1)
    result = sock.connect_ex((target, port))
    if result == 0:
        print(f"Port {port} is OPEN")
    sock.close()
