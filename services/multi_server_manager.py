from monitor import Monitor
from services.server_manager import ServerManager

class MultiServerManager:

    def __init__(self):
        self.manager = ServerManager()

    def hostname_all(self):
        servers = self.manager.get_servers()
        for server in servers:
            print("=" * 50)
            print(server["name"])
            print("=" * 50)
            monitor = Monitor(server)
            print(monitor.hostname())
            monitor.close()

    def memory_all(self):
        servers = self.manager.get_servers()
        for server in servers:
            print("=" * 50)
            print(server["name"])
            print("=" * 50)
            monitor = Monitor(server)
            print(monitor.memory())
            monitor.close()

    def cpu_all(self):
        servers = self.manager.get_servers()
        for server in servers:
            print("=" * 50)
            print(server["name"])
            print("=" * 50)
            monitor = Monitor(server)
            print(monitor.cpu())
            monitor.close()

    def disk_all(self):
        servers = self.manager.get_servers()
        for server in servers:
            print("=" * 50)
            print(server["name"])
            print("=" * 50)
            monitor = Monitor(server)
            print(monitor.disk())
            monitor.close()

    def uptime_all(self):
        servers = self.manager.get_servers()
        for server in servers:
            print("=" * 50)
            print(server["name"])
            print("=" * 50)
            monitor = Monitor(server)
            print(monitor.uptime())
            monitor.close()

    def ip_all(self):
        servers = self.manager.get_servers()
        for server in servers:
            print("=" * 50)
            print(server["name"])
            print("=" * 50)
            monitor = Monitor(server)
            print(monitor.ip())
            monitor.close()

