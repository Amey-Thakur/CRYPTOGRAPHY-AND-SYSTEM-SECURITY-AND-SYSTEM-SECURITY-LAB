# Experiment 7: Nmap Scanning & OS Fingerprinting
# Course: System Security Lab (CSL604)
# Name: Amey Thakur (https://github.com/Amey-Thakur)
# Roll No: 50
# Batch: B3
# Repository: https://github.com/Amey-Thakur/CRYPTOGRAPHY-AND-SYSTEM-SECURITY-AND-SYSTEM-SECURITY-LAB
# Date: April 04, 2021

"""
Experiment 7: Download and install Nmap. Use it with different options to scan open ports, 
perform OS fingerprinting, do a ping scan etc.

Description:
This script acts as a wrapper for Nmap, allowing the user to execute standard scans 
programmatically. It demonstrates the use of subprocess to invoke the 'nmap' command-line tool.

Requirements:
- Python 3.x
- Nmap installed and added to PATH (https://nmap.org/download.html)

Usage:
> python Nmap_Scanner.py
"""

import subprocess
import sys

def run_nmap(command):
    """
    Executes the nmap command and prints output.
    """
    print(f"\n[+] Executing: {command}")
    print("-" * 60)
    try:
        # Use shell=True for windows command parsing if needed, but array is safer
        # Splitting command string into list for subprocess
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        
        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                print(output.strip())
        
        rc = process.poll()
        print("-" * 60)
        return rc
    except FileNotFoundError:
        print("[!] Error: Nmap not found. Please install Nmap and add it to your PATH.")
        return -1
    except Exception as e:
        print(f"[!] Error: {e}")
        return -1

def main():
    target = input("Enter Target IP (e.g., 127.0.0.1 or scanme.nmap.org): ").strip()
    if not target:
        target = "scanme.nmap.org"
        print(f"[*] utilizing default target: {target}")

    while True:
        print("\n--- Nmap Scanner Menu ---")
        print("1. Intense Scan          (nmap -T4 -A -v <target>)")
        print("2. Service Version Scan  (nmap -sV <target>)")
        print("3. OS Detection          (nmap -O <target>)")
        print("4. IP Protocol Scan      (nmap -sO <target>)")
        print("5. Interface List        (nmap --iflist)")
        print("6. Exit")
        
        choice = input("Select scan type (1-6): ").strip()

        if choice == '1':
            run_nmap(f"nmap -T4 -A -v {target}")
        elif choice == '2':
            run_nmap(f"nmap -sV {target}")
        elif choice == '3':
            run_nmap(f"nmap -O {target}")
        elif choice == '4':
            run_nmap(f"nmap -sO {target}")
        elif choice == '5':
            # Run on localhost/current machine
            run_nmap("nmap --iflist")
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("[!] Invalid choice.")

if __name__ == "__main__":
    main()
