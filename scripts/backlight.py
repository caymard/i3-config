import subprocess

process = subprocess.check_output(["xbacklight", "-get"])
output = process.decode("utf-8")
output = output.split(".")[0]
print(output)
