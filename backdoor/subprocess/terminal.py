import subprocess


# Popen -> Old Interface
# run : execute the command and wait for the result

while True:
    command = input("Command : ")
    if command == "exit":
        break
    results = subprocess.run("ls -l ", shell=True, capture_output=True, universal_newlines=True) # macos command

    # print(results.stdout.decode("utf-8", errors="ignore"))
    print(results.stdout)
    print(results.stderr)
