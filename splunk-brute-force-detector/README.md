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


---

✅ Once you've pasted this into `README.md`, save and push it:

```bash
git add README.md
git commit -m "Final full README with structure, SPL, alerting, and visuals"
git push
