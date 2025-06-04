# 🔐 Secure Keystroke Logger

A Python-based, secure keystroke logging tool designed for **controlled cybersecurity environments**, **ethical hacking labs**, and **system behavior monitoring**. This tool captures user keystrokes, stores them in timestamped log files, and encrypts them using AES-based symmetric encryption (`Fernet`). It also includes optional input blocking via Windows API to simulate advanced security scenarios.

> ⚠️ This tool is intended **strictly for ethical and educational purposes**. Unauthorized or malicious use is strictly prohibited and may violate local and international laws.

---

## 🚀 Features

- ✅ **Real-time Keystroke Logging**  
  Captures both regular and special keys (Shift, Ctrl, etc.)

- 🔒 **AES Encryption with Fernet**  
  All log files are encrypted using a password-derived key

- 🕒 **Timestamped File Naming**  
  Each log file is uniquely named using the current date and time

- 🛡️ **Input Blocking (Windows)**  
  Uses `ctypes` to disable user input until logging is stopped

- 📁 **Auto Directory Management**  
  Creates the logging directory if it doesn’t exist

---

## 🧰 Tech Stack

- **Python 3.6+**
- `pynput` – For keyboard event listening
- `cryptography` – For AES-based Fernet encryption
- `ctypes` – Windows API for input blocking
- `threading` – Background thread for blocking input

---

## 📦 Installation

### Prerequisites
Ensure Python is installed. Then install dependencies

---

## ⚙️ Configuration

LOG_DIR = r"C:\Your\Preferred\Log\Directory"
PASSWORD = "YourStrongPassword"

---

## ▶️ Usage

1. Run the script:
python secure_keylogger.py
2. The logger will start in the background, logging keystrokes.
3. Press Esc to:
    Stop logging
    Automatically encrypt the .txt file
    Delete the original (plaintext) log

---

## 🔐 Encryption Overview

1. Method: AES (via cryptography.fernet)
2. Key: Password padded to 32 bytes and base64 encoded
3. Output: .enc encrypted file in the same log directory
4. Security: Original .txt file is securely deleted after encryption

---

## ⚠️ Disclaimer
This tool is strictly for:
1. ✅ Cybersecurity labs
2. ✅ Penetration testing (with permission)
3. ✅ Educational demonstrations
4. ✅ Digital forensics & secure behavior analysis

❌ Unauthorized use is illegal and unethical.
Do not install this tool on systems without explicit permission.

I am not responsible for any misuse of this code. Use at your own risk, and always adhere to legal and ethical standards.

--- 

## 📄 License
This project is licensed under the MIT License.
You are free to use, modify, and distribute it under the terms of this license.
