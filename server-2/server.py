import socket

# Define o endereço IP local e a porta para o servidor
SERVER_HOST = '0.0.0.0'  # '0.0.0.0' permite receber conexões de qualquer endereço IP na rede local
SERVER_PORT = 12345      # Escolha uma porta disponível e que esteja aberta

# Cria o socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)  # Escuta uma conexão

print(f"Servidor rodando na porta {SERVER_PORT}. Aguardando conexão...")

# Aceita uma conexão de um cliente
client_socket, client_address = server_socket.accept()
print(f"Cliente {client_address} conectado.")

# Recebe e envia mensagens
try:
    while True:
        # Recebe mensagem do cliente
        message = client_socket.recv(1024).decode('utf-8')
        if not message:
            break
        print(f"Cliente: {message}")

        # Envia uma resposta para o cliente
        response = input("Digite uma resposta para o cliente: ")
        client_socket.send(response.encode('utf-8'))
finally:
    client_socket.close()
    server_socket.close()
    print("Conexão encerrada.")
