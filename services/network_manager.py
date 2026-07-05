class NetworkManager:

    def __init__(self,monitor):
        self.monitor = monitor

    def menu(self):
        while True:
            print("\n" + "=" * 40)
            print(" NETWORK INFORMATION ")
            print("=" * 40)
            print("1. IP Address")
            pritn("2. Default Gateway")
            print("3. DNS")
            print("4. Open Ports")
            print("5. Back")
            print("=" * 40)

            choice = input("Choose: ")

            if choice == "1":
                print("\nIP Address:")
                print(self.monitor.ip_address())
            elif choice == "2":
                print("\nDefault Gateway:")
                print(self.monitor.gateway())
            elif choice == "3":
                print("\nDNS:")
                print(self.monitor.dns())
            elif choice == "4":
                print("\nOpen Ports:")
                print(self.monitor.open_ports())
            elif choice == "5":
                break
            else:
                print("Invalid Choice")
