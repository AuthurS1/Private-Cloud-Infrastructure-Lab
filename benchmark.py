import time

from services.server_manager import ServerManager
from services.thread_health import ThreadHealth

manager = ServerManager()
servers = manager.get_servers()
health = ThreadHealth()
start = time.time()
health.run(servers)
end = time.time()
print()
print(f"Execution Time: {end-start:.2f} seconds")

