# Experiment 3: Hashing Algorithms (MD5 & SHA-1 Analysis)
# Course: System Security Lab (CSL604)
# Name: Amey Thakur (https://github.com/Amey-Thakur)
# Roll No: 50
# Batch: B3
# Repository: https://github.com/Amey-Thakur/CRYPTOGRAPHY-AND-SYSTEM-SECURITY-AND-SYSTEM-SECURITY-LAB
# Date: 12/03/2021

import hashlib

"""
Objective:
To demonstrate and compare the output characteristics (Digest Size, Raw Bytes, Hex Representation)
of MD5 and SHA-1 hashing algorithms using the same input message.

Input Message: "AMEY"
"""

print("Message : AMEY")

# ----------------- MD5 Demonstration -----------------
# Generate MD5 hash of byte string b"AMEY"
result_bytes = hashlib.md5(b"AMEY").hexdigest()

# Generate MD5 hash of string "AMEY" encoded as standard UTF-8
result_str = hashlib.md5("AMEY".encode("utf-8")).hexdigest()

# Create MD5 hash object
m = hashlib.md5(b"AMEY")

print("\n--- MD5 Algorithm ---")
print("Hash Algorithm : ", m.name)
print("Digest Size (in bytes) : ", m.digest_size) 
print("Raw Bytes : ", m.digest())    # Output in raw bytes
print("Hex Representation : ", m.hexdigest()) # Output in hexadecimal

# ----------------- SHA-1 Demonstration -----------------
# Generate SHA-1 hash of byte string b"AMEY"
result_sha1_bytes = hashlib.sha1(b"AMEY").hexdigest()

# Generate SHA-1 hash of string "AMEY" encoded as standard UTF-8
result_sha1_str = hashlib.sha1("AMEY".encode("utf-8")).hexdigest()

# Create SHA-1 hash object
m = hashlib.sha1(b"AMEY")

print("\n--- SHA-1 Algorithm ---")
print("Hash Algorithm : ", m.name)
print("Digest Size (in bytes) : ", m.digest_size) 
print("Raw Bytes : ", m.digest())    # Output in raw bytes
print("Hex Representation : ", m.hexdigest()) # Output in hexadecimal
