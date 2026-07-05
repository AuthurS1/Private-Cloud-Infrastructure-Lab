import paramiko


class SSHClient:
    def __init__(self, server):
        self.server = server
        self.client = paramiko.SSHClient()

        #Tu dong chap nhan host key moi
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        #Ket noi SSH bang SSH Key
        self.client.connect(
            hostname=self.server["host"],
            port=self.server["port"],
            username=self.server["username"],
            key_filename=self.server["ssh_key"],
            timeout=10
)

    def execute(self, command):
        stdin, stdout, stderr = self.client.exec_command(command)

        output = stdout.read().decode()
        error = stderr.read().decode()

        return output,error

    def close(self):
        self.client.close()
