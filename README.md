# 🚀 CyberSecurity Tools Repository

A collection of Python security tools I built while practicing ethical hacking, penetration testing, and scripting.  
Every tool is designed to help in real-world security tasks and strengthen Python skills related to cybersecurity.

---

## 📌 Tools Included

---

### 1️⃣ Password Generator 🔐

A tool for generating secure passwords.

**Features:**
- Strong random password generator  
- Option to include special characters  
- Supports generating multiple passwords at once  
- Warns when password length is weak  
- Saves results to `passwords.txt`

**Run:**

**Example Output:**
$ python password_generator.py

Enter password length: 12

Include special characters? (y/n): y

Generated Password:  $Ka93@uQpL#2

Do you want to save the password to a file? (y/n): y

Password saved successfully ✔


### 2️⃣ Advanced Port Scanner 🔎

A multi-threaded port scanner similar to mini-Nmap.

**Features:**
- Multi-Threading → very fast scanning  
- Banner Grabbing (Service Detection)  
- Saves results automatically into a report file (`scan_target.txt`)  
- Scans custom port range  
- CLI argument support  

**Run using CLI Arguments:**
**Output Example:**
Scanning Target: 8.8.8.8

🟢 Port 53 OPEN → DNS 

🟢 Port 80 OPEN → HTTP 

 Scan Completed ✔ 
 
 Report saved as scan_8_8_8_8.txt

