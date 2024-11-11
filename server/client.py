import socket

# Define o endereço IP e a porta do servidor
SERVER_HOST = '192.168.56.1'  # Substitua pelo IP do servidor
SERVER_PORT = 12345

# Cria o socket TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_HOST, SERVER_PORT))

print("Conectado ao servidor.")

try:
    while True:
        # Envia uma mensagem ao servidor
        message = input("Digite uma mensagem para o servidor: ")
        if message.lower() == 'sair':
            break
        client_socket.send(message.encode('utf-8'))

        # Recebe resposta do servidor
        response = client_socket.recv(1024).decode('utf-8')
        print(f"Resposta do servidor: {response}")
finally:
    client_socket.close()
    print("Conexão encerrada.")
