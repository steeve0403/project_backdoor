# ---------- Sockets network : Server ----------
import socket

HOST_IP = "127.0.0.1"
HOST_PORT = 32000
MAX_DATA_SIZE = 1024

def socket_received_all_data(socket_p, data_len):
    current_data_len = 0
    total_data = None
    # print(f"Socket receive all data length: {data_len}")
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

print(f"Wait for the connection on {HOST_IP}, port {HOST_PORT}...")
connection_socket, client_address = s.accept()
print(f"Connection is established whith {client_address}")

dl_filename = None

while True:
    infos_data = socket_send_and_receive_all_data(connection_socket, "infos")
    if not infos_data:
        break
    command = input(f"{client_address[0]} : {str(client_address[1])}  {infos_data.decode()} > ")

    command_split = command.split(" ")
    if len(command_split) == 2 and command_split[0] == "dl":
        dl_filename = command_split[1]

    data_received = socket_send_and_receive_all_data(connection_socket, command)
    if not data_received:
        break

    if dl_filename:
        if len(data_received) == 1 and data_received == b" ":
            print(f"Error: file {dl_filename} not found.")
        else:
            file = open(dl_filename, "wb")
            file.write(data_received)
            file.close()
            print(f"File : {dl_filename} downloaded")
        dl_filename = None
    else:
        print(data_received.decode())


s.close()
connection_socket.close()