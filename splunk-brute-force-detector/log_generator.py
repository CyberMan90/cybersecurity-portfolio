import csv
from datetime import datetime, timedelta
import random

usernames = ['admin', 'jdoe', 'hacker01', 'msmith']
ips = ['192.168.1.' + str(i) for i in range(2, 10)]
statuses = ['success', 'failure']
locations = ['US', 'RU', 'DE']
devices = ['Windows10', 'macOS', 'Ubuntu']

rows = []
now = datetime.now()

for i in range(200):
    row = {
        'timestamp': (now - timedelta(minutes=random.randint(0, 60))).isoformat(),
        'username': random.choice(usernames),
        'src_ip': random.choice(ips),
        'status': random.choices(statuses, weights=[0.3, 0.7])[0],
        'location': random.choice(locations),
        'device': random.choice(devices)
    }
    rows.append(row)

with open('sample_logs.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)

print("✅ Log file generated: sample_logs.csv")

