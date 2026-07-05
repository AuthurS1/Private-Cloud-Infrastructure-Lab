from ssh_client import SSHClient

ssh = SSHClient()

output, error = ssh.execute("hostname")

print("OUTPUT:")
print(output)

print("ERROR:")
print(error)

ssh.close()

