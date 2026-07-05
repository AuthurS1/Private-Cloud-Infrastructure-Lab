from monitor import Monitor
from services.server_manager import ServerManager
from utils.status import check_usage

class HealthCheck:
    def __init__(self):
        self.manager = ServerManager()

    def run(self):
        servers = self.manager.get_servers()
        print()
        print("=" * 70)
        print("SERVER HEALTH CHECK")
        print("=" * 70)

        print(
            f"{'Server':15}"
            f"{'CPU':22}"
            f"{'RAM':22}"
            f"{'Disk':22}"
            f"{'Service'}"
        )

        print("-" * 100)

        for server in servers:
            monitor = Monitor(server)
            cpu_value = monitor.cpu_usage()
            ram_value = monitor.memory_usage()
            disk_value = monitor.disk_usage()

            cpu = f"{cpu_value}% {check_usage(cpu_value)}"
            ram = f"{ram_value}% {check_usage(ram_value)}"
            disk = f"{disk_value}% {check_usage(disk_value)}"

            if server["name"] == "webserver01":
                service = monitor.nginx().strip()
            elif server["name"] == "database01":
                service == monitor.mariadb().strip()
            else:
                service = "Unknown"
            print(
                f"{server['name']:15}"
                f"{cpu:22}"
                f"{ram:22}"
                f"{disk:22}"
                f"{service}"
            )
            monitor.close()

