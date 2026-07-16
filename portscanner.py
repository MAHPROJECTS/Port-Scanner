#pythons built in networking tool
import socket
import threading
#lets python talk to operating system
import subprocess


#prodding device
def ping_device(ip):

    result = subprocess.run(
        #sending one ping
        ["ping", "-n", "1", ip],
        #hiding output
        stdout=subprocess.DEVNULL
    )
    #checking success
    if result.returncode == 0:
        return True

    else:
        return False



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

#ask for netwrok
subnet = input("Enter subnet")

#generate every ip on subnet
for host in range(1, 255):

    ip = f"{subnet}.{host}"

    print(ip)



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

        service = services.get(port, "Unknown")

        banner = grab_banner(port)

        print(f"\nPort {port}: OPEN")
        print(f"Service: {service}")
        print(f"Banner: {banner}")

        open_ports.append(port)

    sock.close()



#connects sends requests recieves response

def grab_banner(port):

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        sock.settimeout(1)

        sock.connect((target, port))

        # send a simple HTTP request
        if port == 80 or port == 443:
            sock.send(
                b"GET / HTTP/1.1\r\nHost: example.com\r\n\r\n"
            )

        banner = sock.recv(1024)

        sock.close()

        return banner.decode(errors="ignore").strip()

    except:
        return "No banner"


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
