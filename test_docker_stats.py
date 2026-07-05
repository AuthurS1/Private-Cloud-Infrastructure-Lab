from monitor import Monitor
from services.server_manager import ServerManager

manager = ServerManager()
server = manager.get_servers()[0]
monitor = Monitor(server)

print("=" * 60)
print("DOCKER STATS")
print("=" * 60)

print(monitor.docker_stats())

monitor.close()

