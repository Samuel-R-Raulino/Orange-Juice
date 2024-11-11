import socket
import threading

# Define o endereço IP e a porta do servidor
SERVER_HOST = '0.0.0.0'  # '0.0.0.0' permite conexões de outros computadores
SERVER_PORT = 12345

# Cria o socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(5)  # Define o limite máximo de conexões pendentes

print(f"Servidor rodando em {SERVER_HOST}:{SERVER_PORT}")

# Função para lidar com cada cliente
def handle_client(client_socket, client_address):
    print(f"[NOVA CONEXÃO] {client_address} conectado.")
    while True:
        try:
            # Recebe dados do cliente
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"[{client_address}] {message}")

            # Envia uma resposta ao cliente
            client_socket.send("Mensagem recebida".encode('utf-8'))
        except:
            break

    print(f"[DESCONECTADO] {client_address} desconectou.")
    client_socket.close()

# Loop principal para aceitar conexões
while True:
    client_socket, client_address = server_socket.accept()
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()
