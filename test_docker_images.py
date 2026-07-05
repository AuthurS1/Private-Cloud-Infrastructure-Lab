from monitor import Monitor
from services.server_manager import ServerManager

manager = ServerManager()
server = manager.get_servers()[0]
monitor = Monitor(server)

print("=" * 60)
print("DOCKER IMAGES")
print("=" * 60)

print(monitor.docker_images())

monitor.close()

