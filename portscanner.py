#pythons built in networking tool
import socket
import threading


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
#mulitple threads running so place to save all results
open_ports = []

#ask sthe user for target IP and then that turns into the varibale taret192.168.1.109
target = input("Enter target IP or hostname: ")

start_port = int(input("Start port: "))
end_port = int(input("End port: "))


#crreates socket, gives timout, tests port , check if it workksed
def scan_port(port):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.settimeout(0.2)

    result = sock.connect_ex((target, port))

    if result == 0:
        print(f"Port {port}: OPEN")

        open_ports.append(port)

    sock.close()



#creates threads waits for them to finish and joins them
threads = []

for port in range(start_port, end_port + 1):

    thread = threading.Thread(
        target=scan_port,
        args=(port,)
    )

    threads.append(thread)

    thread.start()

    for thread in threads:
        thread.join()





print("\nScanning:", target)
print("----------------------------")
