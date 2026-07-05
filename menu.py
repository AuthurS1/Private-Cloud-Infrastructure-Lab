class Menu:

    @staticmethod
    def show():
        print("\n" + "=" * 40)
        print(" SERVER MANAGEMENT SYSTEM")
        print("=" * 40)
        print("1. Server Infomation")
        print("2. Resource Monitoring")
        print("3. Service Management")
        print("4. Network Information")
        print("5. Generate Report")
        print("5. Exit")
        print("=" * 40)

        return input("Choose: ")

class ServiceMenu:
    @staticmethod
    def show():

        print("\n" + "=" * 40)
        print(" SERVICE MANAGEMENT ")
        print("=" * 40)
        print("1. Check Nginx Status")
        print("2. Start Nginx")
        print("3. Stop Nginx")
        print("4. Restart Nginx")
        print("5. Back")
        print("=" * 40)

        return input("Choose: ")

class NetworkMenu:
    @staticmethod
    def show():
        print("\n" + "=" * 40)
        print(" NETWORK INFORMATION ")
        print("=" * 40)
        print("1. IP Address")
        print("2. Default Gateway")
        print("3. DNS")
        print("4. Open Ports")
        print("5. Back")
        print("=" * 40)

        return input("Choose: ")

