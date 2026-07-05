from services.server_manager import ServerManager
from services.thread_health import ThreadHealth

manager = ServerManager()

servers = manager.get_servers()
health = ThreadHealth()
results = health.run(servers)

print()

for server in results:
    print(server)

