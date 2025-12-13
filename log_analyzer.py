# ====== Expanded Log Analyzer ======

def analyze_logs(file_path):
    stats = {"INFO": 0, "WARNING": 0, "ERROR": 0}
    failed_logins = []

    with open(file_path, "r") as file:
        for line in file:
            # Count log levels
            for level in stats:
                if level in line:
                    stats[level] += 1
            # Detect failed login attempts
            if "Failed login attempt" in line:
                failed_logins.append(line.strip())

    return stats, failed_logins

# Analyze the expanded log file
stats, failed_logins = analyze_logs("expanded_logs.txt")

# Print summary
print("=== Log Level Summary ===")
for level, count in stats.items():
    print(f"{level}: {count}")

print("\n=== Failed Login Attempts ===")
for entry in failed_logins:
    print(entry)
