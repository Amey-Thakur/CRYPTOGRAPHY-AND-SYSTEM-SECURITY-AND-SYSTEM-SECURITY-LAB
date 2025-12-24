<!-- =========================================================================================
                                     HEADER SECTION
     ========================================================================================= -->
<div align="center">

  # System Security Lab

  ### CSL604 · Semester VI · Computer Engineering

  [![Curated by](https://img.shields.io/badge/Curated%20by-Amey%20Thakur-blue.svg)](https://github.com/Amey-Thakur)
  [![Documents](https://img.shields.io/badge/Documents-10-yellowgreen.svg)](#laboratory-experiments)
  [![Language](https://img.shields.io/badge/Language-Python%20%7C%20Java-blueviolet.svg)](./)

  **A comprehensive collection of laboratory experiments for System Security, covering cryptographic algorithms, network security protocols, packet sniffing, and vulnerability assessments.**

  ---

  **[How to Use](#how-to-use)** &nbsp;·&nbsp; **[Learning Path](#learning-path)** &nbsp;·&nbsp; **[Experiment 1](#experiment-1-product-cipher-substitution--transposition)** &nbsp;·&nbsp; **[Experiment 2](#experiment-2-rsa--digital-signature)** &nbsp;·&nbsp; **[Experiment 3](#experiment-3-hashing--performance-analysis)** &nbsp;·&nbsp; **[Experiment 4](#experiment-4-network-reconnaissance)** &nbsp;·&nbsp; **[Experiment 5](#experiment-5-packet-sniffing-telnet)** &nbsp;·&nbsp; **[Experiment 6](#experiment-6-arp-spoofing)** &nbsp;·&nbsp; **[Experiment 7](#experiment-7-nmap-scanning--os-fingerprinting)** &nbsp;·&nbsp; **[Experiment 8](#experiment-8-sql-injection)** &nbsp;·&nbsp; **[Experiment 9](#experiment-9-denial-of-service-dos)** &nbsp;·&nbsp; **[Experiment 10](#experiment-10-email-security-pgp)**

</div>

---

> [!TIP]
> **Practical Application**: This lab bridging theory and practice. You won't just implement algorithms like RSA and MD5 in Python; you will also actively engage with powerful network security tools such as **Wireshark** for packet analysis, **Nmap** for reconnaissance, and **Ettercap** for ARP spoofing simulations.

> [!WARNING]
> **Ethical Hacking**: Experiments involving packet sniffing, SQL injection, and buffer overflow are for educational purposes only. Ensure you perform these simulations in a controlled, isolated environment (sandbox) and never on unauthorized networks or systems.

---

<!-- =========================================================================================
                                     HOW TO USE SECTION
     ========================================================================================= -->
## How to Use

### Environment Setup
Ensure you have **Python 3.x** installed. Some experiments require external tools and libraries:
- **Python Libraries**: Install `scapy` for packet manipulation experiments.
  ```bash
  pip install scapy
  ```
- **External Tools**:
  - **Nmap**: Required for Experiment 7.
  - **Wireshark**: Required for packet analysis in Experiment 5.
  - **GPGwin**: Required for PGP implementation in Experiment 10.

### Running Experiments
1. **Clone the repository**:
   ```bash
   git clone https://github.com/Amey-Thakur/CRYPTOGRAPHY-AND-SYSTEM-SECURITY-AND-SYSTEM-SECURITY-LAB.git
   ```
2. **Navigate** to the specific experiment directory:
   ```bash
   cd "System Security Lab/Experiment-X"
   ```
3. **Execute** the Python script (ensure you have administrative privileges for network operations):
   ```bash
   python script_name.py
   ```

### Laboratory Reports
Each experiment includes a detailed PDF report covering:
- **Problem Statement**: The specific security challenge addressed.
- **Theory**: The underlying cryptographic or networking concepts.
- **Implementation**: Code explanation and execution screenshots.
- Use these reports as a reference for structuring your own lab submissions.

---

<!-- =========================================================================================
                                     LEARNING PATH SECTION
     ========================================================================================= -->
## Learning Path

### Phase 1: Cryptographic Algorithms
Focus on the mathematical foundations of security.
- **Experiment 1 & 2**: Implement Product Ciphers and RSA to understand encryption mechanics.
- **Experiment 3**: Analyze Hashing Algorithms (MD5/SHA-1) for data integrity verification.

### Phase 2: Network Intelligence
Master the tools used for gathering information and monitoring traffic.
- **Experiment 4**: Perform Network Reconnaissance using `whois`, `dig`, and `traceroute`.
- **Experiment 5**: Intercept and analyze unencrypted traffic with Packet Sniffing (Telnet).
- **Experiment 7**: Conduct advanced Port Scanning and OS Fingerprinting using Nmap.

### Phase 3: Offensive Security
Simulate attacks to understand defensive requirements.
- **Experiment 6**: Execute ARP Spoofing to demonstrate Man-in-the-Middle attacks.
- **Experiment 8**: Exploit web vulnerabilities using SQL Injection techniques.
- **Experiment 9**: Simulate Denial-of-Service (DoS) attacks to test system resilience.

### Phase 4: Applied Security
Implement security measures in real-world applications.
- **Experiment 10**: Secure communications using PGP (Pretty Good Privacy) for email encryption.

---

<!-- =========================================================================================
                                     EXPERIMENT 1
     ========================================================================================= -->
## Experiment 1: Product Cipher (Substitution & Transposition)

Design and Implementation of a product cipher using Substitution and Transposition ciphers.

**Date:** January 29, 2021

| # | Document | Description | Link |
|:-:|:---|:---|:-:|
| 1 | **Product_Cipher.py** | Product Cipher Implementation | [View](Experiment-1/Product_Cipher.py) |
| 2 | **Substitution_Cipher.py** | Substitution Cipher Logic | [View](Experiment-1/Substitution_Cipher.py) |
| 3 | **Transposition_Cipher.py** | Transposition Cipher Logic | [View](Experiment-1/Transposition_Cipher.py) |
| 4 | Lab Report (PDF) | Detailed experiment report | [View](Experiment-1/Amey_B-50_System_Security_Lab_Experiment-1.pdf) |
| 5 | Lab Report (DOCX) | Editable report file | [Download](Experiment-1/Amey_B-50_System_Security_Lab_Experiment-1.docx) |

---

<!-- =========================================================================================
                                     EXPERIMENT 2
     ========================================================================================= -->
## Experiment 2: RSA & Digital Signature

Implementation and analysis of RSA cryptosystem and Digital signature scheme using RSA/El Gamal.

**Date:** February 11, 2021

| # | Document | Description | Link |
|:-:|:---|:---|:-:|
| 1 | **RSA.py** | RSA Algorithm Implementation | [View](Experiment-2/RSA.py) |
| 2 | **RSA_Math.py** | Modular Arithmetic Utilities | [View](Experiment-2/RSA_Math.py) |
| 3 | Lab Report (PDF) | Detailed experiment report | [View](Experiment-2/Amey_B-50_System_Security_Lab_Experiment-2.pdf) |
| 4 | Lab Report (DOCX) | Editable report file | [Download](Experiment-2/Amey_B-50_System_Security_Lab_Experiment-2.docx) |

---

<!-- =========================================================================================
                                     EXPERIMENT 3
     ========================================================================================= -->
## Experiment 3: Hashing & Performance Analysis

For varying message sizes, test the integrity of the message using MD-5, SHA-1, and analyze the performance of the two protocols. Use crypt APIs.

**Date:** February 18, 2021

| # | Document | Description | Link |
|:-:|:---|:---|:-:|
| 1 | **MD5.py** | MD5 Hashing Implementation | [View](Experiment-3/MD5.py) |
| 2 | **SHA1.py** | SHA-1 Hashing Implementation | [View](Experiment-3/SHA1.py) |
| 3 | **MD5_SHA1.py** | Comparison Script | [View](Experiment-3/MD5_SHA1.py) |
| 4 | **Available_Algorithms.py** | Algorithm Lister | [View](Experiment-3/Available_Algorithms.py) |
| 5 | Lab Report (PDF) | Detailed experiment report | [View](Experiment-3/Amey_B-50_System_Security_Lab_Experiment-3.pdf) |
| 6 | Lab Report (DOCX) | Editable report file | [Download](Experiment-3/Amey_B-50_System_Security_Lab_Experiment-3.docx) |

---

<!-- =========================================================================================
                                     EXPERIMENT 4
     ========================================================================================= -->
## Experiment 4: Network Reconnaissance

Study the use of network reconnaissance tools like WHOIS, dig, traceroute, nslookup to gather information about networks and domain registrars.

**Date:** March 09, 2021

| # | Document | Description | Link |
|:-:|:---|:---|:-:|
| 1 | **Network_Reconnaissance.py** | Network Reconnaissance Script | [View](Experiment-4/Network_Reconnaissance.py) |
| 2 | Lab Report (PDF) | Detailed experiment report | [View](Experiment-4/Amey_B-50_System_Security_Lab_Experiment-4.pdf) |
| 3 | Lab Report (DOCX) | Editable report file | [Download](Experiment-4/Amey_B-50_System_Security_Lab_Experiment-4.docx) |

---

<!-- =========================================================================================
                                     EXPERIMENT 5
     ========================================================================================= -->
## Experiment 5: Packet Sniffing (Telnet)

Design a network and implement packet sniffing on telnet traffic using Wireshark.

**Date:** March 30, 2021

| # | Document | Description | Link |
|:-:|:---|:---|:-:|
| 1 | **Packet_Sniffer.py** | Packet Sniffing (Scapy) | [View](Experiment-5/Packet_Sniffer.py) |
| 2 | Lab Report (PDF) | Detailed experiment report | [View](Experiment-5/Amey_B-50_System_Security_Lab_Experiment-5.pdf) |
| 3 | Lab Report (DOCX) | Editable report file | [Download](Experiment-5/Amey_B-50_System_Security_Lab_Experiment-5.docx) |

---

<!-- =========================================================================================
                                     EXPERIMENT 6
     ========================================================================================= -->
## Experiment 6: ARP Spoofing

Implement ARP spoofing using Ettercap.

**Date:** April 20, 2021

| # | Document | Description | Link |
|:-:|:---|:---|:-:|
| 1 | **ARP_Spoofer.py** | ARP Spoofing Script (Scapy) | [View](Experiment-6/ARP_Spoofer.py) |
| 2 | Lab Report (PDF) | Detailed experiment report | [View](Experiment-6/Amey_B-50_System_Security_Lab_Experiment-6.pdf) |
| 3 | Lab Report (DOCX) | Editable report file | [Download](Experiment-6/Amey_B-50_System_Security_Lab_Experiment-6.docx) |

---

<!-- =========================================================================================
                                     EXPERIMENT 7
     ========================================================================================= -->
## Experiment 7: Nmap Scanning & OS Fingerprinting

Download and install Nmap. Use it with different options to scan open ports, perform OS fingerprinting, do a ping scan etc.

**Date:** April 04, 2021

| # | Document | Description | Link |
|:-:|:---|:---|:-:|
| 1 | **Nmap_Scanner.py** | Nmap Automation Script | [View](Experiment-7/Nmap_Scanner.py) |
| 2 | Lab Report (PDF) | Detailed experiment report | [View](Experiment-7/Amey_B-50_System_Security_Lab_Experiment-7.pdf) |
| 3 | Lab Report (DOCX) | Editable report file | [Download](Experiment-7/Amey_B-50_System_Security_Lab_Experiment-7.docx) |

---

<!-- =========================================================================================
                                     EXPERIMENT 8
     ========================================================================================= -->
## Experiment 8: SQL Injection

Perform SQL injection on a vulnerable website.

**Date:** April 20, 2021

| # | Document | Description | Link |
|:-:|:---|:---|:-:|
| 1 | **SQL_Injection_Tester.py** | SQL Injection (sqlmap wrapper) | [View](Experiment-8/SQL_Injection_Tester.py) |
| 2 | Lab Report (PDF) | Detailed experiment report | [View](Experiment-8/Amey_B-50_System_Security_Lab_Experiment-8.pdf) |
| 3 | Lab Report (DOCX) | Editable report file | [Download](Experiment-8/Amey_B-50_System_Security_Lab_Experiment-8.docx) |

---

<!-- =========================================================================================
                                     EXPERIMENT 9
     ========================================================================================= -->
## Experiment 9: Denial-of-Service (DoS)

Simulate DOS attack using Hping, hping3 and other tools.

**Date:** April 20, 2021

| # | Document | Description | Link |
|:-:|:---|:---|:-:|
| 1 | **DoS_Attack_Simulator.py** | DoS Simulation (hping3 wrapper) | [View](Experiment-9/DoS_Attack_Simulator.py) |
| 2 | Lab Report (PDF) | Detailed experiment report | [View](Experiment-9/Amey_B-50_System_Security_Lab_Experiment-9.pdf) |
| 3 | Lab Report (DOCX) | Editable report file | [Download](Experiment-9/Amey_B-50_System_Security_Lab_Experiment-9.docx) |

---

<!-- =========================================================================================
                                     EXPERIMENT 10
     ========================================================================================= -->
## Experiment 10: Email Security (PGP)

Explore the GPGwin tool and implement email security.

**Date:** April 20, 2021

| # | Document | Description | Link |
|:-:|:---|:---|:-:|
| 1 | **PGP_Email_Security.py** | PGP/GPG Wrapper Script | [View](Experiment-10/PGP_Email_Security.py) |
| 2 | Lab Report (PDF) | Detailed experiment report | [View](Experiment-10/Amey_B-50_System_Security_Lab_Experiment-10.pdf) |
| 3 | Lab Report (DOCX) | Editable report file | [Download](Experiment-10/Amey_B-50_System_Security_Lab_Experiment-10.docx) |

---

<!-- =========================================================================================
                                     FOOTER SECTION
     ========================================================================================= -->
<div align="center">

  <!-- Footer Navigation -->
  **[↑ Back to Top](#system-security-lab)**

  **[How to Use](#how-to-use)** &nbsp;·&nbsp; **[Learning Path](#learning-path)** &nbsp;·&nbsp; **[Experiment 1](#experiment-1-product-cipher-substitution--transposition)** &nbsp;·&nbsp; **[Experiment 2](#experiment-2-rsa--digital-signature)** &nbsp;·&nbsp; **[Experiment 3](#experiment-3-hashing--performance-analysis)** &nbsp;·&nbsp; **[Experiment 4](#experiment-4-network-reconnaissance)** &nbsp;·&nbsp; **[Experiment 5](#experiment-5-packet-sniffing-telnet)** &nbsp;·&nbsp; **[Experiment 6](#experiment-6-arp-spoofing)** &nbsp;·&nbsp; **[Experiment 7](#experiment-7-nmap-scanning--os-fingerprinting)** &nbsp;·&nbsp; **[Experiment 8](#experiment-8-sql-injection)** &nbsp;·&nbsp; **[Experiment 9](#experiment-9-denial-of-service-dos)** &nbsp;·&nbsp; **[Experiment 10](#experiment-10-email-security-pgp)**

  <br>

  **[🏠 Back to Main Repository](../)**

</div>

---

<div align="center">

  ### [Cryptography and System Security and System Security Lab](https://github.com/Amey-Thakur/CRYPTOGRAPHY-AND-SYSTEM-SECURITY-AND-SYSTEM-SECURITY-LAB)

  **CSL604 · Semester VI · Computer Engineering**

  *University of Mumbai · Curated by [Amey Thakur](https://github.com/Amey-Thakur)*

</div>
