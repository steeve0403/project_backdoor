# ---------- Sockets network : Server ----------
import socket

HOST_IP = "127.0.0.1"
HOST_PORT = 32000
MAX_DATA_SIZE = 1024

def socket_received_all_data(socket_p, data_len):
    current_data_len = 0
    total_data = None
    print(f"Socket receive all data length: {data_len}")
    while current_data_len < data_len:
        chunk_len = data_len - current_data_len
        if chunk_len > MAX_DATA_SIZE:
            chunk_len = MAX_DATA_SIZE
        data = socket_p.recv(chunk_len)
        if not data:
            return None
        if not total_data:
            total_data = data
        else:
            total_data += data
        current_data_len += len(data)

    return total_data

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST_IP, HOST_PORT))
s.listen()

print(f"Attente de connexion sur {HOST_IP}, port {HOST_PORT}...")
connection_socket, client_address = s.accept()
print(f"Connexion établie avec {client_address}")

while True:
    command = input("Command: ")
    if command == "":
        continue
    connection_socket.sendall(command.encode())

    header_data = socket_received_all_data(connection_socket, 13)
    length_data = int(header_data.decode())

    data_received = socket_received_all_data(connection_socket, length_data)
    if not data_received:
        break
    print(f"data received: {data_received}")
    print(data_received.decode())

s.close()
connection_socket.close()