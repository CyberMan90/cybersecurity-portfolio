## 🛡️ Security Incident: Public Exposure of AWS Access Key

### 📌 Summary

During the course of this AWS auditing project, a simulated IAM user's access key (`audit-user`) was accidentally exposed via a public GitHub commit. AWS automatically detected the leaked key, triggered an automated quarantine, and opened a security support case.

---

### 🧭 What Happened

- A `.numbers` spreadsheet containing access credentials was unintentionally committed to GitHub
- The access key (`AKIAQA3RL2ZOLURKXRVR`) became publicly accessible in the repo:
  `https://github.com/CyberMan90/cybersecurity-portfolio/blob/...`
- AWS detected the exposure and automatically applied the `AWSCompromisedKeyQuarantineV3` policy to the `audit-user`, restricting its access

---

### 🛠️ Incident Response Steps

✅ **Step 1: Rotated Credentials**
- Created a new access key for the user
- Inactivated and deleted the exposed key

✅ **Step 2: Investigated Activity**
- Downloaded and reviewed CloudTrail logs
- Verified no unauthorized access, resource abuse, or policy changes occurred

✅ **Step 3: Cleanup**
- Detached the quarantine policy from the IAM user
- Removed the `.numbers` file from the repo
- Updated `.gitignore` to exclude future sensitive files

✅ **Step 4: Notification & Confirmation**
- Responded to the AWS support case confirming remediation was complete

---

### 🔐 Lessons Learned

- ⚠️ Always scan for secrets before committing — tools like [`git-secrets`](https://github.com/awslabs/git-secrets) or GitHub secret scanning are invaluable
- 🔑 Never store sensitive credentials in plaintext, even in testing environments
- 📦 Simulated IAM users should be handled with real-world caution
- 🧯 Enable MFA on all IAM accounts
- 🕵️ Monitor CloudTrail logs and AWS Support cases regularly

---

### 📚 Why This Matters

This real-world security event served as a practical test of incident response skills:

- Triage and remediation of a leaked credential
- CloudTrail analysis to confirm no compromise
- Coordination with AWS Support
- Post-mortem reflection and hardening of future processes

> "Security isn't just about avoiding mistakes. It's about how quickly and effectively you respond when they happen."

