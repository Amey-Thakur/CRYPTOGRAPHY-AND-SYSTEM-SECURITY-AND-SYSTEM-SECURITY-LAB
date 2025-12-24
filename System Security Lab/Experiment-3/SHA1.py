# Experiment 3: Hashing Algorithms (SHA-1)
# Course: System Security Lab (CSL604)
# Name: Amey Thakur (https://github.com/Amey-Thakur)
# Roll No: 50
# Batch: B3
# Repository: https://github.com/Amey-Thakur/CRYPTOGRAPHY-AND-SYSTEM-SECURITY-AND-SYSTEM-SECURITY-LAB
# Date: 12/03/2021

import hashlib

"""
Theory:
SHA-1 (Secure Hash Algorithm 1) is a cryptographic hash function which takes 
an input and produces a 160-bit (20-byte) hash value typically rendered as 
a 40-digit hexadecimal number.

This program demonstrates:
1. Generating SHA-1 hashes for different input strings.
2. Converting the input strings to integers (Base 32) to observe input differences.
"""

# 1. Initializing strings
str1 = "MEGA"
str2 = "ARCHIT"
str3 = "SAAKSHI"

# 2. Hashing using SHA-1
# encode() converts the string to bytes.
result1 = hashlib.sha1(str1.encode())
result2 = hashlib.sha1(str2.encode())
result3 = hashlib.sha1(str3.encode())

# 3. Printing the Hexadecimal Digest
print("The hexadecimal equivalent of SHA1 is : ", end ="") 
print(result1.hexdigest())
print(result2.hexdigest())
print(result3.hexdigest())

# 4. Input Analysis (Base 32 Conversion)
# Converting the input strings to their integer representation using Base 32.
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
