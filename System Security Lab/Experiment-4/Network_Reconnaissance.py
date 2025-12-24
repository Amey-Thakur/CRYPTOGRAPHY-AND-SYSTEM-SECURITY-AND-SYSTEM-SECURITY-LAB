# Experiment 4: Network Reconnaissance  Tools
# Course: System Security Lab (CSL604)
# Name: Amey Thakur (https://github.com/Amey-Thakur)
# Roll No: 50
# Batch: B3
# Repository: https://github.com/Amey-Thakur/CRYPTOGRAPHY-AND-SYSTEM-SECURITY-AND-SYSTEM-SECURITY-LAB
# Date: 09/03/2021

import os
import sys

"""
Objective:
Study the use of network reconnaissance tools like WHOIS, DIG, TRACEROUTE, NSLOOKUP 
to gather information about networks and domain registrars.

This script demonstrates the usage of these tools via Python's system calls.
Note: Ensure 'whois' and 'dig' are installed and in your system PATH.
      (Common on Linux/macOS, requires installation on Windows).
"""

def print_separator(title):
    print("\n" + "="*60)
    print(f" {title}")
    print("="*60 + "\n")

target_domain = input("Enter target domain (e.g., google.com): ")
if not target_domain:
    target_domain = "google.com"

# 1. WHOIS
# Retrieves domain registration details (Registrar, Registrant, Dates, Name Servers).
print_separator(f"1. WHOIS ({target_domain})")
os.system(f"whois {target_domain}")

# 2. NSLOOKUP
# Queries DNS to obtain domain name or IP address mapping.
print_separator(f"2. NSLOOKUP ({target_domain})")
os.system(f"nslookup {target_domain}")

# 3. TRACEROUTE (tracert on Windows)
# Traces the path that a packet takes to reach the destination.
print_separator(f"3. TRACEROUTE ({target_domain})")
if sys.platform == "win32":
    os.system(f"tracert {target_domain}")
else:
    os.system(f"traceroute {target_domain}")

# 4. DIG
# Domain Information Groper - detailed DNS query tool.
print_separator(f"4. DIG ({target_domain})")
os.system(f"dig {target_domain}")

print("\n" + "="*60)
print(" Network Reconnaissance Completed")
print("="*60 + "\n")
