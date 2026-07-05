from monitor import Monitor
from services.server_manager import ServerManager

manager = ServerManager()
servers = manager.get_servers()

print("=" * 60)
print("DOCKER VERSION")
print("=" * 60)

for server in (servers):
    monitor = Monitor(server)
    version = monitor.docker_version()
    print(f"Server: {server['name']}")

    if version:
        print(version)
    else:
        print("Docker not installed")
    print("=" * 60)

    monitor.close()

