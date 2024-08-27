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

def socket_send_and_receive_all_data(socket_p, command):
    if not command: # if command == "":
        return
    socket_p.sendall(command.encode())

    header_data = socket_received_all_data(socket_p, 13)
    length_data = int(header_data.decode())

    data_received = socket_received_all_data(socket_p, length_data)
    return data_received




s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST_IP, HOST_PORT))
s.listen()

print(f"Attente de connexion sur {HOST_IP}, port {HOST_PORT}...")
connection_socket, client_address = s.accept()
print(f"Connexion établie avec {client_address}")

while True:
    infos_data = socket_send_and_receive_all_data(connection_socket, "infos")
    if not infos_data:
        break
    command = input(f"{client_address[0]} : {client_address[1]}  {infos_data.decode()} > ")
    data_received = socket_send_and_receive_all_data(connection_socket, command)
    if not data_received:
        break
    print(data_received.decode())


s.close()
connection_socket.close()