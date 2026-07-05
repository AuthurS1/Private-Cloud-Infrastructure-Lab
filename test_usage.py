from services.server_manager import ServerManager
from monitor import Monitor

manager = ServerManager()
server = manager.list_servers()
monitor = Monitor(server)

print("Connected to:", server["name"])
print()


print("CPU :", monitor.cpu_usage(), "%")
print("RAM :", monitor.memory_usage(), "%")
print("Disk :", monitor.disk_usage(), "%")

monitor.close()

