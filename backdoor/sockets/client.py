# ---------- Sockets network : Client ----------
import socket

HOST_IP = "127.0.0.1"
HOST_PORT = 32000

s = socket.socket()

print(f"Connection at server: {HOST_IP}, port: {HOST_PORT} ....")
s.connect((HOST_IP, HOST_PORT))
print(f"Connected to server.")

s.close()