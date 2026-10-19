from collections import Counter
from pathlib import Path

# Read our fictional security log
log_file = Path(__file__).with_name("security.log")
lines = log_file.read_text(encoding="utf-8").splitlines()

failed_ips = []

# Look for failed login events
for line in lines:
    if "WARNING Login failed" in line:
        for field in line.split():
            if field.startswith("ip="):
                failed_ips.append(field.removeprefix("ip="))
                break

# Count failures from each IP
counts = Counter(failed_ips)

print("=== SECURITY LOG ANALYSIS ===")
print(f"Total failed logins: {len(failed_ips)}")

for ip, count in counts.most_common():
    print(f"{ip}: {count} failed login(s)")

    if count >= 3:
        print("  ALERT: Repeated failed logins detected!")