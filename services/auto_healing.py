from monitor import Monitor
from utils.logger import logger

class AutoHealing:
    SERVICES = {
        "webserver01": {
            "name": "Nginx",
            "status": "nginx",
            "restart": "restart_nginx",
        },

        "database01": {
              "name": "MariaDB",
              "status": "mariadb",
              "restart": "restart_mariadb",
        }
    }

    def fix(self, server):
        monitor = Monitor(server)
        config = self.SERVICES.get(server["name"])
        if config:
            status = getattr(monitor, config["status"])().strip()
            if status not in ["Running", "active"]:
                print(f"{server['name']} : {config['name']} DOWN")
                logger.warning(
                    f"{server['name']} : Restart {config['name']}"
                )
                getattr(monitor, config["restart"])()
                print("Restarted")
            else:
                print(f"{server['name']} : {config['name']} OK")
        monitor.close()
