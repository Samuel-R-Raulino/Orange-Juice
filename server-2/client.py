import socket

# Substitua pelo IP do servidor
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
SERVER_HOST = local_ip
SERVER_PORT = 12345  # A mesma porta usada no servidor

# Cria o socket TCP para o cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_HOST, SERVER_PORT))

print(f"Conectado ao servidor em {SERVER_HOST}:{SERVER_PORT}")

# Envia e recebe mensagens
try:
    while True:
        # Envia uma mensagem para o servidor
        message = input("Digite uma mensagem para o servidor: ")
        client_socket.send(message.encode('utf-8'))

        # Recebe resposta do servidor
        response = client_socket.recv(1024).decode('utf-8')
        if not response:
            break
        print(f"Servidor: {response}")
finally:
    client_socket.close()
    print("Conexão encerrada.")
