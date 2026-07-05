from services.auto_healing import AutoHealing
from services.server_manager import ServerManager

manager = ServerManager()
servers = manager.get_servers()
healing = AutoHealing()

for server in servers:
    healing.fix(server)

