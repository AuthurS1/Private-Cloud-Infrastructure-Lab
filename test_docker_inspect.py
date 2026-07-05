from monitor import Monitor
from services.server_manager import ServerManager

manager = ServerManager()
server = manager.get_servers()[0]
monitor = Monitor(server)

name = input("Container name: ")

print("=" * 60)
print("DOCKER INSPECT")
print("=" * 60)

print(monitor.docker_inspect(name))

monitor.close()

