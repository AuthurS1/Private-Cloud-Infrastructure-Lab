import json

class ServerManager:

    def __init__(self):
        self.file = "config/servers.json"

    def get_servers(self):
        with open(self.file, "r") as f:
            data = json.load(f)
        return data["servers"]

    def list_servers(self):
        servers = self.get_servers()

        print("\n" + "=" * 40)
        print(" SERVER LIST ")
        print("=" * 40)

        for i, server in enumerate(servers, start=1):
            print(f"{i}. {server['name']} ({server['host']})")

        print("=" * 40)
        choice = int(input("\nSelect server: "))
        return servers[choice - 1]
