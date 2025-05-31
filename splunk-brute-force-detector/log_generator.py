import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()
logs = []

# Set up user base
users = [fake.user_name() for _ in range(50)]
normal_ips = [fake.ipv4_public() for _ in range(25)]
attack_ip = fake.ipv4_public()  # One malicious IP

# Generate normal login events
for _ in range(850):
    logs.append({
        "timestamp": (datetime.now() - timedelta(minutes=random.randint(0, 1440))).strftime('%Y-%m-%d %H:%M:%S'),
        "username": random.choice(users),
        "src_ip": random.choice(normal_ips),
        "status": random.choices(["success", "failure"], weights=[0.9, 0.1])[0],
        "location": fake.city(),
        "device": fake.user_agent()
    })

# Simulate brute-force attack from attacker IP
attacker_username_pool = [fake.user_name() for _ in range(10)]
for _ in range(150):
    logs.append({
        "timestamp": (datetime.now() - timedelta(minutes=random.randint(0, 60))).strftime('%Y-%m-%d %H:%M:%S'),
        "username": random.choice(attacker_username_pool),
        "src_ip": attack_ip,
        "status": "failure",
        "location": fake.city(),
        "device": fake.user_agent()
    })

# Shuffle the list to randomize event order
random.shuffle(logs)

# Save to CSV
df = pd.DataFrame(logs)
df.to_csv("sample_logs.csv", index=False)

print("✅ Generated 1000 login events (normal + brute force) and saved to sample_logs.csv")

