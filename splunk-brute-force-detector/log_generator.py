#!/usr/bin/env python3
"""
log_generator.py

Simulates login activity and outputs to CSV for use in Splunk or SIEM projects.

Features:
- Generates realistic login attempts (successes and failures)
- Includes fields: timestamp, username, src_ip, status, location, device
- Supports CLI arguments to customize output
"""

import csv
import random
import argparse
import logging
from datetime import datetime, timedelta

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Sample data pools
usernames = ['admin', 'msmith', 'jdoe', 'hacker01']
devices = ['Windows10', 'Ubuntu', 'macOS']
locations = ['US', 'RU', 'CN', 'DE']
statuses = ['success', 'failure']

def generate_logs(count):
    """Generates a list of simulated login event dictionaries."""
    logs = []
    base_time = datetime.now()

    for _ in range(count):
        timestamp = base_time - timedelta(minutes=random.randint(1, 120))
        entry = {
            'timestamp': timestamp.isoformat(),
            'username': random.choice(usernames),
            'src_ip': f"192.168.1.{random.randint(2, 99)}",
            'status': random.choices(statuses, weights=[0.7, 0.3])[0],
            'location': random.choice(locations),
            'device': random.choice(devices),
        }
        logs.append(entry)

    return logs

def write_csv(logs, output_file):
    """Writes a list of login events to a CSV file."""
    fieldnames = ['timestamp', 'username', 'src_ip', 'status', 'location', 'device']
    with open(output_file, mode='w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(logs)
    logging.info(f"{len(logs)} log entries written to {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Simulate login logs for brute-force detection.")
    parser.add_argument('--count', type=int, default=50, help='Number of log entries to generate')
    parser.add_argument('--output', type=str, default='sample_logs.csv', help='Output CSV file name')

    args = parser.parse_args()

    logging.info(f"Generating {args.count} simulated login logs...")
    logs = generate_logs(args.count)
    write_csv(logs, args.output)
    logging.info("Done.")

if __name__ == '__main__':
    main()
