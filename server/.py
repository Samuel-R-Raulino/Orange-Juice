import socket
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

print(f"Endereço IP local: {local_ip}")