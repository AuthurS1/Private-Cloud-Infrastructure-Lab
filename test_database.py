from services.server_manager import ServerManager
from monitor import Monitor

manager = ServerManager()

server = manager.list_servers()

monitor = Monitor(server)

print("\nConnected to:", server["name"])

print("\nMariaDB Status:")

print(monitor.mariadb())

monitor.close()
