# Experiment 10: Email Security (PGP/GPG)
# Course: System Security Lab (CSL604)
# Name: Amey Thakur (https://github.com/Amey-Thakur)
# Roll No: 50
# Date: April 20, 2021

"""
Experiment 10: Explore the GPGwin tool and implement email security.

Description:
This script acts as a wrapper for the 'gpg' command-line tool (part of Gpg4win or GnuPG).
It allows the user to programmatically perform PGP key management, encryption, and signing operations,
mirroring the functionality of GUI tools like Kleopatra.

Requirements:
- Python 3.x
- Gpg4win or GnuPG installed and added to PATH (https://gpg4win.org/)

Usage:
> python PGP_Email_Security.py
"""

import subprocess
import sys

def run_gpg(command):
    """
    Executes the gpg command.
    """
    print(f"\n[+] Executing: {command}")
    print("-" * 60)
    try:
        # GPG often prompts for passphrases via pinentry (GUI) or TTY.
        # This script assumes the environment is set up for such prompts if needed.
        subprocess.run(command, shell=True)
        print("\n" + "-" * 60)
    except KeyboardInterrupt:
        print("\n[!] Interrupted by user.")
    except Exception as e:
        print(f"[!] Error: {e}")

def main():
    print("--- PGP Email Security Automation (GPG wrapper) ---")
    
    while True:
        print("\n1. List Public Keys          (gpg --list-keys)")
        print("2. List Secret Keys          (gpg --list-secret-keys)")
        print("3. Generate New Key Pair     (gpg --full-generate-key)")
        print("4. Encrypt a File            (gpg -e -r <recipient> <file>)")
        print("5. Decrypt a File            (gpg -d <file>)")
        print("6. Sign a File (Detached)    (gpg -b <file>)")
        print("7. Verify Signature          (gpg --verify <sig_file> <data_file>)")
        print("8. Exit")

        choice = input("\nSelect Operation (1-8): ").strip()

        if choice == '1':
            run_gpg("gpg --list-keys")
        
        elif choice == '2':
            run_gpg("gpg --list-secret-keys")

        elif choice == '3':
            print("Follow the on-screen prompts to generate your key pair.")
            run_gpg("gpg --full-generate-key")

        elif choice == '4':
            filename = input("Enter filename to encrypt: ").strip()
            recipient = input("Enter recipient email/ID: ").strip()
            if filename and recipient:
                run_gpg(f"gpg --encrypt --recipient {recipient} {filename}")

        elif choice == '5':
            filename = input("Enter filename to decrypt (e.g., file.txt.gpg): ").strip()
            if filename:
                run_gpg(f"gpg --decrypt {filename}")

        elif choice == '6':
            filename = input("Enter filename to sign: ").strip()
            if filename:
                run_gpg(f"gpg --detach-sign {filename}")

        elif choice == '7':
            sig_file = input("Enter signature filename (e.g., file.txt.sig): ").strip()
            data_file = input("Enter original filename (optional, press Enter if inferred): ").strip()
            cmd = f"gpg --verify {sig_file}"
            if data_file:
                cmd += f" {data_file}"
            run_gpg(cmd)

        elif choice == '8':
            print("Exiting...")
            break
        else:
            print("[!] Invalid choice.")

if __name__ == "__main__":
    main()
