# Experiment 1: Product Cipher (Substitution & Transposition)
# Course: System Security Lab (CSL604)
# Name: Amey Thakur (https://github.com/Amey-Thakur)
# Roll No: 50
# Batch: B3
# Repository: https://github.com/Amey-Thakur/CRYPTOGRAPHY-AND-SYSTEM-SECURITY-AND-SYSTEM-SECURITY-LAB
# Date: 29/01/2021

"""
Theory:
Product Cipher is a method of encryption that combines two or more transformations, 
such as Substitution and Transposition, to result in a cipher that is more secure 
than the individual components.

This program demonstrates the Substitution Cipher component, specifically a Caesar Cipher,
where each letter in the plaintext is shifted by a fixed number of positions down the alphabet.
"""

key = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(n, plaintext):
    """
    Encrypts the plaintext using a Substitution Cipher (Caesar Cipher).
    
    Logic:
    The algorithm iteratively shifts each character of the plaintext by a fixed value 'n'.
    The modulo 26 operation ensures the shift wraps around the alphabet (e.g., 'z' shifts to 'a').
    
    Args:
        n (int): The shift key (offset), determining the number of positions to shift.
        plaintext (str): The input message to be encrypted.
        
    Returns:
        str: The resulting ciphertext after encryption.
    """
    result = ''

    for l in plaintext.lower():
        try:
            # key.index(l): Find the 0-based index of the character in the alphabet.
            # + n: Apply the shift (key).
            # % 26: Wrap around if the index exceeds 25 (length of alphabet).
            i = (key.index(l) + n) % 26
            result += key[i]
        except ValueError:
            # If the character 'l' is not found in 'key' (e.g., space, punctuation, numbers),
            # it is appended to the result without modification.
            result += l

    return result.lower()

def decrypt(n, ciphertext):
    """
    Decrypts the ciphertext using a Substitution Cipher (Caesar Cipher).
    
    Logic:
    Reverses the encryption process by shifting each character backward by 'n' positions.
    modulo 26 is again used to handle negative wrapping (e.g., 'a' shifts back to 'z').
    
    Args:
        n (int): The shift key (offset) used for encryption.
        ciphertext (str): The message to be decrypted.
        
    Returns:
        str: The decrypted plaintext.
    """
    result = ''

    for l in ciphertext:
        try:
            # key.index(l): Find the index of the encrypted character.
            # - n: Reverse the shift.
            # % 26: Handle wrapping for negative values (e.g., -1 % 26 = 25).
            i = (key.index(l) - n) % 26
            result += key[i]
        except ValueError:
            # If character is not in the key, keep it as is.
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
