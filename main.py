from monitor import Monitor
from menu import Menu, NetworkMenu
from services.service_manager import ServiceManager
from services.network_manager import NetworkManager
from services.report_manager import ReportManager
from services.docker_manager import DockerManager

monitor = Monitor(server)
service = ServiceManager(monitor)
network = NetworkManager(monitor)
report = ReportManager(monitor)
docker = DockerManager(monitor)

while True:
    choice = Menu.show()

    if choice == "1":
        print("\nHostname:")
        print(monitor.hostname())

        print("\nUptime:")
        print(monitor.uptime())

    elif choice == "2":
        print("\nCPU:")
        print(monitor.cpu())

        print("\nMemory:")
        print(monitor.memory())

        print("\nDisk:")
        print(monitor.disk())

    elif choice == "3":
        service.menu()
    elif choice == "4":
        network.menu()

    elif choice == "5":
        report.generate()

    elif choice == "6":
        monitor.close()
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")
