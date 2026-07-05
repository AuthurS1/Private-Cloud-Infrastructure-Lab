from flask import Flask, render_template, jsonify
from monitor import Monitor
from services.server_manager import ServerManager

app = Flask(__name__)

manager = ServerManager()

@app.route("/")
def home():
    servers = manager.get_servers()
    data = []
    for server in servers:
        monitor = Monitor(server)

        if server["name"] == "webserver01":
            service = monitor.nginx().strip()
        elif server["name"] == "database01":
            service = monitor.mariadb().strip()
        else:
            service = "Unknown"
        data.append({
            "name": server["name"],
            "cpu": monitor.cpu_usage(),
            "ram": monitor.memory_usage(),
            "disk": monitor.disk_usage(),
            "service": service,
        })
        monitor.close()
    return render_template(
       "index.html",
       servers=data
    )

@app.route("/api/status")
def status():
    servers = manager.get_servers()
    data = []
    for server in servers:
        monitor = Monitor(server)
        if server["name"] == "webserver01":
            service = monitor.nginx().strip()
        elif server["name"] == "database01":
            service = monitor.mariadb().strip()
        else:
            service = "Unknown"

        data.append({
            "name":server["name"],
            "cpu":monitor.cpu_usage(),
            "ram":monitor.memory_usage(),
            "disk":monitor.disk_usage(),
            "service":service
        })
        monitor.close()
    return jsonify(data)

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False,
    )

