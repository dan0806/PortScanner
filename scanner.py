import socket
import concurrent.futures
from sys import argv, exit

def scan_port(target_ip, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1)
        connection = s.connect_ex((target_ip, port))

        if connection == 0:
            print(f"[OPEN] Port {port}")


def port_scan(target_ip, initial_port, last_port):
    print(f"Scanning target {target_ip}")

    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        futures = []
        for port in range(initial_port, last_port + 1):
            future = executor.submit(scan_port, target_ip, port)
            futures.append(future)

        for future in concurrent.futures.as_completed(futures):
            future.result()
    print("\nScan completed")


if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: python scanner.py <ip> <initial port> <last port>")
        exit()

    target_ip = argv[1]

    try:
        socket.gethostbyname(target_ip)
    except socket.gaierror:
        print("Invalid host")
        exit()

    initial_port = int(argv[2])
    last_port = int(argv[3])

    port_scan(target_ip, initial_port, last_port)
