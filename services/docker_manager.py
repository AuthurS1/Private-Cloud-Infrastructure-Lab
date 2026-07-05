class DockerManager:

    def __init__(self, monitor):
        self.monitor = monitor
    def menu(self):
        while True:
            print("\n" + "=" * 40)
            print(" DOCKER MANAGEMENT ")
            print("=" * 40)
            print("1. List Running Containers")
            print("2. List All Container")
            print("3. Start Container")
            print("4. Stop Container")
            print("5. Restart Container")
            print("6. View Logs")
            print("7. Back")
            print("=" * 40)

            choice = input("Choose: ")
            if choice == "1":
                print()
                print(self.monitor.docker_ps())
            elif choice == "2":
                print()
                print(self.monitor.docker_ps_all())
            elif choice == "3":
                name = input("Container Name: ")
                self.monitor.docker_start(name)
                print("Container Started")
            elif choice == "4":
                name = input("Container Name: ")
                self.monitor.docker_stop(name)
                print("Container Stopped")
            elif choice == "5":
                name = input("Container Name: ")
                self.monitor.docker_restart(name)
                print("Container Restarted")
            elif choice == "6":
                name = input("Container Name: ")
                print()
                print(self.monitor.docker_logs(name))
            elif choice == "7":
                break
            else:
                print("Invalid Choice")

