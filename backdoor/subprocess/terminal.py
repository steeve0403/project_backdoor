import subprocess


# Popen -> Old Interface
# run : execute the command and wait for the result

results = subprocess.run("ls -l ", shell=True, capture_output=True, universal_newlines=True) # macos command

# print(results.stdout.decode("utf-8", errors="ignore"))
print(results.stdout)
print(results.stderr)
