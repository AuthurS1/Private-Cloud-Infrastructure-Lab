from monitor import Monitor
from services.server_manager import ServerManager

manager = ServerManager()
servers = manager.get_servers()

print()
print("=" * 75)
print("DOCKER SUMMARY")
print("=" * 75)

print(
    f"{'Server':15}"
    f"{'Containers':15}"
    f"{'Images':10}"
    f"{'Networks':12}"
    f"{'Volumes':}"
)

print("=" * 75)

for server in servers:
    monitor = Monitor(server)
    if monitor.docker_version():
        print(
            f"{server['name']:15}"
            f"{monitor.docker_container_count():15}"
            f"{monitor.docker_image_count():10}"
            f"{monitor.docker_network_count():12}"
            f"{monitor.docker_volume_count()}"
        )
    else:
        print(
            f"{server['name']:15}"
            f"{'Docker Not Installed'}"
        )
    monitor.close()
