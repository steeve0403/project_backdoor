# ---------- Sockets network : Server ----------
import socket

HOST_IP = "127.0.0.1"
HOST_PORT = 32000

s = socket.socket()
# s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#  To solve the problem "already used" on Windows, you need to add an option to the socket.
s.bind((HOST_IP, HOST_PORT))
s.listen()

print(f"Waiting for connection on {HOST_IP}, port {HOST_PORT} ....")
connection_socket, client_address = s.accept()
print(f"Accepted connection from {client_address}")

text_to_send = "Hello"

connection_socket.sendall(text_to_send.encode())

s.close()
connection_socket.close()

