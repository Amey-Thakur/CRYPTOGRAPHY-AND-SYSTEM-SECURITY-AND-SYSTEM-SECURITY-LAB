# Experiment 3: Hashing Algorithms (MD5 & SHA-1) - Available Algorithms
# Course: System Security Lab (CSL604)
# Name: Amey Thakur (https://github.com/Amey-Thakur)
# Roll No: 50
# Batch: B3
# Repository: https://github.com/Amey-Thakur/CRYPTOGRAPHY-AND-SYSTEM-SECURITY-AND-SYSTEM-SECURITY-LAB
# Date: 18/02/2021

import hashlib 

"""
Objective:
To list all the hashing algorithms guaranteed to be supported by the 'hashlib' module
across all platforms.
"""

# prints all available algorithms 
print ("The available algorithms are : ", end ="") 
print (hashlib.algorithms_guaranteed) 
