# 🛡️ Splunk Brute Force Attack Detector

This project simulates brute-force login attempts and detects them using **Splunk**, a leading SIEM platform. It demonstrates hands-on skills in log simulation, threat detection, SPL querying, dashboard creation, and alerting — essential for blue teamers, SOC analysts, and cybersecurity professionals.

---

## 🧠 What You'll Learn

- How to simulate authentication logs (Python)
- How to ingest and normalize data in Splunk
- How to write SPL queries for threat detection
- How to build dashboards with actionable visuals
- How to configure real-time alerts based on detection logic

---

## 🗂️ Project Structure

```bash
splunk-brute-force-detector/
├── log_generator.py              # Generates 1000 simulated login events
├── sample_logs.csv               # Output CSV (brute force + normal)
├── requirements.txt              # Python dependencies
├── .gitignore                    # Git tracking exclusions
├── LICENSE                       # MIT license
├── README.md                     # This file!
├── search_queries/
│   └── brute_force_detection.spl # SPL logic to detect brute-force attempts
└── splunk_screenshots/
    └── dashboard.png             # Final Splunk dashboard screenshot
```

---

## 🚀 How It Works

### ✅ 1. Generate Logs

```bash
python3 log_generator.py
```
Creates a CSV file of 1000 login events with:
✅ Normal login attempts (success/failure)
✅ Brute-force pattern from a single IP

---

### ✅ 2. Ingest into Splunk

1. Go to **Settings → Add Data → Upload**
2. Select `sample_logs.csv`
3. Set:
   - **Source Type**: `custom:auth_logs`
   - **Index**: `brute_force_test` (create if needed)
4. Confirm parsing preview
5. Click **Submit**

---

### ✅ 3. Detect Brute Force in SPL

```
index=brute_force_test sourcetype="custom:auth_logs"
| stats count by src_ip, status
| where status="failure" AND count > 5
| sort -count
```
This query identifies any IP with more than 5 failed login attempts — a common brute-force threshold.

---

## 📊 Dashboard Preview

Includes four panels:

1. **Brute Force Detection by IP** – Table of suspicious IPs  
2. **Login Trends Over Time** – Line chart (success/failure breakdown)  
3. **Success vs Failure Login Breakdown** – Pie chart  
4. **Top Failed Login Usernames** – Bar chart of targeted accounts

---

## 📸 Screenshot:

---

## 🔔 Real-Time Alerting

This project includes a Splunk alert that automatically triggers when brute-force login behavior is detected.

---

## 🎯 Trigger Conditions
More than 5 login failures from the same IP

Runs every 5 minutes (via cron)

Time window: last 15 minutes

---

## 🛠️ How to Configure
Go to Search & Reporting → Search

Paste the detection SPL:
```
index=brute_force_test sourcetype="custom:auth_logs"
| stats count by src_ip, status
| where status="failure" AND count > 5
| sort -count
```
Click Save As → Alert

Use the following settings:

| Field               | Value                        |
|---------------------|------------------------------|
| Title               | Brute Force IP Detection     |
| Alert Type          | Scheduled                    |
| Time Range          | Last 15 minutes              |
| Cron Schedule       | `*/5 * * * *` (Every 5 mins) |
| Trigger Condition   | Number of results > 0        |
| Trigger             | Once per result              |
| Severity            | Medium                       |
| Action              | Add to Triggered Alerts / Email |


---

## ⚖️ Why Use Medium Severity?
Brute-force attempts are suspicious and require triage

But not always confirmed threats (e.g. scanners, login test scripts)

Escalate to High if attempts increase or target multiple users

---

### ✅ This alert mimics real-world SOC response logic and is ready to be expanded with notifications or scripts.

---

## 🛠️ Setup (Python Environment)
bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

---

## 📄 License

MIT License – free to use, modify, and share.

---

## 👨🏽‍💻 Author

CyberMan90
GitHub: CyberMan90

