import os
import subprocess


# Popen -> Old Interface
# run : execute the command and wait for the result

while True:
    command = input(os.getcwd() + " > ")
    if command == "exit":
        break

    command_split = command.split(" ")
    if len(command_split) == 2 and command_split[0] == "cd":
        try:
            os.chdir(command_split[1])
        except FileNotFoundError:
            print("Error: No such file or directory")
    else:
        results = subprocess.run(command, shell=True, capture_output=True, universal_newlines=True) # macos command

        # print(results.stdout.decode("utf-8", errors="ignore"))
        print(results.stdout)
        print(results.stderr)
