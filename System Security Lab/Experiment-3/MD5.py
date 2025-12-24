# Experiment 3: Hashing & Performance Analysis thms (MD5)
# Course: System Security Lab (CSL604)
# Name: Amey Thakur (https://github.com/Amey-Thakur)
# Roll No: 50
# Batch: B3
# Repository: https://github.com/Amey-Thakur/CRYPTOGRAPHY-AND-SYSTEM-SECURITY-AND-SYSTEM-SECURITY-LAB
# Date: 18/02/2021

import hashlib

"""
Theory:
MD5 (Message-Digest Algorithm 5) is a widely used cryptographic hash function 
that produces a 128-bit (16-byte) hash value. It is typically expressed as a 
32-digit hexadecimal number. 

This program demonstrates:
1. Generating MD5 hashes for different input strings.
2. Converting the input strings to integers (Base 32) to observe input differences.
"""

# 1. Initializing strings
# These are the input messages to be hashed.
str1 = "MEGA"
str2 = "ARCHIT"
str3 = "SAAKSHI"

# 2. Hashing using MD5
# The encode() method converts the string to bytes, which is required by hashlib.
result1 = hashlib.md5(str1.encode())
result2 = hashlib.md5(str2.encode())
result3 = hashlib.md5(str3.encode())

# 3. Printing the Hexadecimal Digest
# hexdigest() returns the encoded data in hexadecimal format.
print("The hexadecimal equivalent of hash is : ", end ="") 
print(result1.hexdigest())
print(result2.hexdigest())
print(result3.hexdigest())

# 4. Input Analysis (Base 32 Conversion)
# Converting the input strings to their integer representation using Base 32.
# This might be used to compare the numerical distance between inputs vs outputs (Avalanche Effect study).
val1 = int(str1, 32)
val2 = int(str2, 32)
val3 = int(str3, 32)

print("The decimal number of hexadecimal string : " + str(val1))
print("The decimal number of hexadecimal string : " + str(val2))
print("The decimal number of hexadecimal string : " + str(val3))

# Calculating differences between the integer values of the inputs
diff1 = val2 - val1
diff2 = val3 - val2

print(" ")
print("The key difference between input 1 and 2 : " + str(diff1))
print("The key difference between input 2 and 3 : " + str(diff2))
