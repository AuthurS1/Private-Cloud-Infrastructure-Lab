from concurrent.futures import ThreadPoolExecutor
from monitor import Monitor

class ThreadHealth:
    def check(self, server):
        monitor = Monitor(server)
        if server["name"] == "webserver01":
            service = monitor.nginx().strip()
        elif server["name"] == "database01":
            service = monitor.mariadb().strip()
        else:
            service = "Unknown"
        result = {
            "server": server["name"],
            "cpu": monitor.cpu_usage(),
            "ram": monitor.memory_usage(),
            "disk": monitor.disk_usage(),
            "service": service,
        }

        monitor.close()

        return result
    def run(self, servers):
        with ThreadPoolExecutor(max_workers=5) as executor:
            results = executor.map(self.check, servers)
        return list(results)
