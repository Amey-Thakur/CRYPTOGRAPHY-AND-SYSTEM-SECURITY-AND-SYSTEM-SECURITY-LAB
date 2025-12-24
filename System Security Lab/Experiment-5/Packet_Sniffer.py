# Experiment 5: Packet Sniffing (Telnet)
# Course: System Security Lab (CSL604)
# Name: Amey Thakur (https://github.com/Amey-Thakur)
# Roll No: 50
# Date: March 30, 2021

"""
Experiment 5: Design a network and implement packet sniffing on telnet traffic using Wireshark.

Description:
This script demonstrates the concept of packet sniffing programmatically using the 'scapy' library.
While Wireshark is a GUI tool for deep analysis, this script shows how to capture and inspect
packets (specifically TCP/Telnet) at the code level.

Requirements:
- Python 3.x
- scapy (pip install scapy)
- Npcap (on Windows) or libpcap (on Linux) for packet capture.

Usage:
Run with administrative privileges (Root/Administrator) to allow packet capture.
> sudo python Packet_Sniffer.py
"""

import sys
from scapy.all import sniff, IP, TCP

def packet_callback(packet):
    """
    Callback function to process each captured packet.
    """
    # Check if the packet has an IP layer
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = packet[IP].proto

        # Check for TCP packets
        if packet.haslayer(TCP):
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
            
            # Filter for Telnet traffic (Port 23)
            # Note: Telnet is unencrypted, so payloads are visible.
            if src_port == 23 or dst_port == 23:
                print(f"[+] Telnet Packet: {src_ip}:{src_port} -> {dst_ip}:{dst_port}")
                
                # Print Payload if present
                if packet.haslayer(TCP) and packet[TCP].playload:
                    print(f"    Payload: {bytes(packet[TCP].payload)}")
            
            else:
                # General TCP Packet
                print(f"[*] TCP Packet: {src_ip}:{src_port} -> {dst_ip}:{dst_port}")

def start_sniffer(interface=None, count=10):
    """
    Starts the packet sniffer.
    """
    print("[-] Starting Packet Sniffer...")
    print(f"[-] Capturing {count} packets...")
    if interface:
        print(f"[-] Interface: {interface}")

    # Sniff packets
    # filter="tcp" restricts capture to TCP protocol
    # prn specifies the callback function
    # count stops after N packets (remove for infinite loop)
    try:
        sniff(iface=interface, filter="tcp", prn=packet_callback, count=count)
        print("[-] Sniffing finished.")
    except Exception as e:
        print(f"[!] Error: {e}")
        print("[!] Ensure you are running as Administrator/Root.")

if __name__ == "__main__":
    # Optional: Allow user to specify interface via command line
    # simple usage for demonstration
    start_sniffer(count=20)
