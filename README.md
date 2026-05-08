# Python_Projects
This repository holds a handful of beginner level cybersecurity projects created using Python! Enjoy :)

⚠️ DISCLAIMER
These projects are intended for educational purposes only. Use them only on systems and networks you own or have explicit permission to test. Unauthorized network scanning or packet sniffing may be illegal.

**Requirements**
Port Scanner - nmap
  pip install python-nmap
Packet Sniffer
  Windows (Run as administrator)

🔐Python Crypto Cipher
A Caesar cipher implementation for encrypting and decrypting messages.

Takes a user-supplied message and numeric key as input
Encrypts the message by shifting letters by the specified key value
Decrypts the ciphertext back to plaintext using the same key
File: Python_Crypto_Cipher/Python_Crypto_Cipher.py


🔑 Python Password Manager
A simple in-memory password manager with account creation and login functionality.

Creates user accounts with SHA-256 hashed passwords
Authenticates users by comparing hashed input against stored hashes
Uses getpass for secure password input (hidden from terminal)
File: Python_Password_Manager/Password_Manager.py


🔒 Python Password Generator
Generates random, secure passwords from a full character set.

Combines uppercase, lowercase, digits, and punctuation characters
Defaults to a 10-character password (configurable via the length parameter)
File: Python_Password_Generator/Password_Generator.py


🌐 Python Port Scanner
A network port scanner built with the python-nmap library.

Scans a target IP address for open ports
Uses Nmap service/version detection (-sV) and default scripts (-sC)
Outputs host state, protocol, port numbers, and port states
File: Python_Port_Scanner/python-nmap.py
Dependency: python-nmap, nmap


📡 Python Packet Sniffer
A low-level network packet sniffer that captures and parses live traffic.

Uses raw sockets to capture IPv4 packets in real time
Parses and displays ICMP, TCP, and UDP packets with detailed header fields
Shows TCP flags (URG, ACK, PSH, RST, SYN, FIN), sequence numbers, and port info
Stops cleanly on KeyboardInterrupt
Note: Requires administrator/root privileges and runs on Windows (uses SIO_RCVALL)
File: Python_Packet_Sniffer/sniffer.py


🔍 Python WHOIS Tool
A lightweight WHOIS lookup tool using raw socket connections.

Queries the IANA WHOIS server on port 43 for domain information
Returns raw WHOIS response data for a given domain
File: Python_WHOIS_Tool/WHOIS_Tool.py

**Usage**

bashpython Python_Crypto_Cipher/Python_Crypto_Cipher.py
python Python_Password_Manager/Password_Manager.py
python Python_Password_Generator/Password_Generator.py
python Python_Port_Scanner/python-nmap.py
python Python_WHOIS_Tool/WHOIS_Tool.py

