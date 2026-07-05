from services.server_manager import ServerManager
from monitor import Monitor

manager = ServerManager()

server = manager.list_servers()

monitor = Monitor(server)

print()

print("Connected to:", server["name"])
print()

print(monitor.hostname())
monitor.close()



