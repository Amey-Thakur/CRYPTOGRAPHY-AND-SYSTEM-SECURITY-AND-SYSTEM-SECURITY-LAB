# Experiment 1: Substitution Cipher
# Course: System Security Lab (CSL604)
# Name: Amey Thakur (https://github.com/Amey-Thakur)
# Roll No: 50
# Batch: B3
# Repository: https://github.com/Amey-Thakur/CRYPTOGRAPHY-AND-SYSTEM-SECURITY-AND-SYSTEM-SECURITY-LAB
# Date: 29/01/2021

"""
Theory:
A substitution cipher is a type of encryption where characters or units of text 
are replaced by others to encrypt a text sequence. 

This program demonstrates a Monoalphabetic Substitution Cipher (Caesar Cipher), 
where each letter in the plaintext is shifted by a fixed number of positions 
down the alphabet.
"""

key = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(n, plaintext):
    """
    Encrypts the plaintext using a Substitution Cipher (Caesar Cipher).
    
    Args:
        n (int): The shift key (offset).
        plaintext (str): The message to be encrypted.
        
    Returns:
        str: The encrypted ciphertext.
    """
    result = ''

    for l in plaintext.lower():
        try:
            # Shift the character index by n and wrap around using modulo 26
            i = (key.index(l) + n) % 26
            result += key[i]
        except ValueError:
            # If character is not in the key (e.g., space, punctuation), keep it as is
            result += l

    return result.lower()

def decrypt(n, ciphertext):
    """
    Decrypts the ciphertext using a Substitution Cipher (Caesar Cipher).
    
    Args:
        n (int): The shift key (offset).
        ciphertext (str): The message to be decrypted.
        
    Returns:
        str: The decrypted plaintext.
    """
    result = ''

    for l in ciphertext:
        try:
            # Shift the character index back by n and wrap around using modulo 26
            i = (key.index(l) - n) % 26
            result += key[i]
        except ValueError:
            # If character is not in the key, keep it as is
            result += l

    return result

# Driver Code
if __name__ == "__main__":
    text = input(str("Enter a message for Encryption: "))
    print("Enter a Key: ")
    offset = input()
    offset = int(offset, 10)

    print("Plaintext: " + text)
    
    # Perform Encryption
    encrypted = encrypt(offset, text)
    print('Encrypted Message: ', encrypted)

    # Perform Decryption
    decrypted = decrypt(offset, encrypted)
    print('Decrypted Message: ', decrypted)
