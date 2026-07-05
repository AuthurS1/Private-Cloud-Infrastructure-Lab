class ServiceManager:

    def __init__(self, monitor):
        self.monitor = monitor

    def menu(self):
        while True:
            print("\n" + "=" * 40)
            print(" SERVICE MANAGEMENT ")
            print("=" * 40)
            print("1. Status")
            print("2. Start")
            print("3. Stop")
            print("4. Restart")
            print("5. Back")
            print("=" * 40)

            choice = input("Choose: ")

            if choice == "1":
                print("\nNginx Status:")
                print(self.monitor.nginx())
            elif choice == "2":
                self.monitor.start_nginx()
                print("Nginx Started")
            elif choice == "3":
                self.monitor.stop_nginx()
                print("Nginx Stopped")
            elif choice == "4":
                self.monitor.restart_nginx()
                print("Nginx Restarted")
            elif choice == "5":
                break
            else:
                print("Invalid Choice")

