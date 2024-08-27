# ---------- Sockets network : Client ----------
import socket
import time

HOST_IP = "127.0.0.1"
HOST_PORT = 32000
MAX_DATA_SIZE = 1024

print(f"Connection at server: {HOST_IP}, port: {HOST_PORT} ....")
while True:
    try:
        s = socket.socket()

        s.connect((HOST_IP, HOST_PORT))
    except ConnectionRefusedError:
        print(f"Error : Unable to connect to server. Reconnection...")
        time.sleep(4)
    else:
        print(f"Connected to server.")
        break


# if received_data:
#     print(received_data.decode())
# else:
#     print("No data")

while True:
    received_data = s.recv(MAX_DATA_SIZE)
    if not received_data:
        break
    print(f"Message received: {received_data.decode()}")
    text_to_send = input("Your message: ")
    s.sendall(text_to_send.encode())


s.close()