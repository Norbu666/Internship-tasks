#Cybersecurity Utilities with Python

Welcome to my internship project repository, developed as part of the **Prodigy InfoTech Cybersecurity Internship**. This repo contains a suite of Python tools focused on security, encryption, monitoring, and analysis — each task designed to strengthen my technical skills and contribute to real-world cybersecurity practice.

## Contents

| Filename                   | Description                                                                 |
|----------------------------|-----------------------------------------------------------------------------|
| `caesar_cypher.py`         | Implements the Caesar Cipher for text encryption and decryption             |
| `image_encrypt&decrypt.py`| Encrypts and decrypts images using pixel-level XOR operations                |
| `keylogger.py`             | Captures keyboard input and logs it locally                                 |
| `packet_sniffer.py`        | Sniffs network traffic and extracts source/destination IP and protocol info |
| `password_checker.py`      | Checks password strength and offers improvement suggestions                 |

---

## Tool Highlights

### Caesar Cipher
- Shift-based encryption using alphabet rotation
- Supports both encryption and decryption
- Useful for understanding classical cryptographic logic

### Image Encryption/Decryption
- Uses `NumPy` & `Pillow` to manipulate pixel data
- Performs bitwise XOR with a key

### keylogger
- Records typed keystrokes
- Educates on data collection and ethical boundaries in monitoring tools

### Packet Sniffer
- Uses raw sockets to capture live network packets
- Parses IP headers to display source/destination addresses and protocol types
- Reinforces low-level network analysis concepts

### Password Strength Checker
- Analyzes input passwords for length, case, digits, and special characters
- Gives personalized feedback to improve security
- Builds awareness around password hygiene

---

## How to Run

Install required libraries:
```bash
pip install pillow numpy


## Run any script
python <script_name>.py

NOTE: Some programs might ask for administrative permission.

