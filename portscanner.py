#pythons built in networking tool
import socket


#creates dictionary of services
services = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    443: "HTTPS",
    3306: "MySQL"
}

#ask sthe user for target IP and then that turns into the varibale taret192.168.1.109
target = input("Enter target IP or hostname: ")

start_port = int(input("Start port: "))
end_port = int(input("End port: "))


print("\nScanning:", target)
print("----------------------------")


for port in range(start_port, end_port + 1):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.settimeout(1)

    result = sock.connect_ex((target, port))


    if result == 0:

        service = services.get(port, "Unknown")

        print(
            f"Port {port}: OPEN ({service})"
        )

    sock.close()
