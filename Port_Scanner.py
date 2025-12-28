import socket
import threading
import argparse

#=============== Command‑Line Arguments ===============
parser = argparse.ArgumentParser(description="Advanced Python Port Scanner")
parser.add_argument("-t", "--target", required=True, help="Target IP or Domain")
parser.add_argument("-s", "--start", type=int, default=1, help="Start Port")
parser.add_argument("-e", "--end", type=int, default=100, help="End Port")

args = parser.parse_args()

target = args.target
start_port = args.start
end_port = args.end

# target = input("Enter target IP or Domain: ")
# start_port = int(input("Start port: "))
# end_port   = int(input("End port: "))

open_ports = []
print(f"\n⚡🚀 Advanced Scanner running on {target} ...\n")

services = {
    21:"FTP", 22:"SSH", 23:"Telnet", 25:"SMTP", 53:"DNS",
    80:"HTTP", 110:"POP3", 143:"IMAP", 443:"HTTPS"
}

def scan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.3)
        result = sock.connect_ex((target, port))

        # ======= Banner Grabbing --> Service Guessing  =========
        if result == 0:
            try:
                banner = sock.recv(1024).decode().strip()
                banner = banner if banner else services.get(port,"Unknown")
            except:
                banner = services.get(port,"Unknown")

            print(f"🟢 Port {port} OPEN → {banner}")
            open_ports.append((port, banner))
    except:
        pass

# ============= Multi‑Threading =======================
threads = []

for port in range(start_port, end_port+1):
    thread = threading.Thread(target=scan, args=(port,))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()


print("\nScan Completed ✔")

#=========== Save Results To Report File ============
if open_ports:
    filename = f"scan_report_{target.replace('.', '_')}.txt"
    with open(filename, "w") as report:
        report.write(f"Scan Report for {target}\n")
        report.write("-"*40 + "\n")
        for p,b in open_ports:
            report.write(f"Port {p} -> {b}\n")

    print(f"\n📝 Report saved as: {filename}")
else:
    print("\nNo open ports to save.")

