import time

from services.health_check import HealthCheck
from services.auto_healing import AutoHealing
from services.server_manager import ServerManager

class Scheduler:
    def __init__(self):
        self.health = HealthCheck()
        self.healing = AutoHealing()
        self.manager = ServerManager()
    def run(self):
        while True:
            print("\n" + "=" * 60)
            print("START MONITORING CYCLE")
            print("=" * 60)

            #Health Check
            self.health.run()

            #Auto Healing
            servers = self.manager.get_servers()

            for server in servers:
                self.healing.fix(server)

            print("\nNext check after 60 minutes...\n")
            time.sleep(5)

