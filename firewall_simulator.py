# ====== Simple Firewall Simulator ======

def load_blocked_ips(file_path):
    blocked = set()
    with open(file_path, "r") as f:
        for line in f:
            blocked.add(line.strip())
    return blocked

def check_ip(ip, blocked_ips):
    if ip in blocked_ips:
        print(f"ACCESS DENIED: {ip} is blocked.")
    else:
        print(f"ACCESS GRANTED: {ip} is allowed.")

# Load blocked IPs
blocked_ips = load_blocked_ips("blocked_ips.txt")

# Test incoming IPs
test_ips = ["192.168.1.10", "192.168.1.20", "10.0.0.5", "8.8.8.8"]

for ip in test_ips:
    check_ip(ip, blocked_ips)
