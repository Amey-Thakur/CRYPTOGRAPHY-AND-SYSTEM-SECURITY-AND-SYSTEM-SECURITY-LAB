# Experiment 1: Product Cipher (Substitution & Transposition)
# Course: System Security Lab (CSL604)
# Name: Amey Thakur (https://github.com/Amey-Thakur)
# Roll No: 50
# Batch: B3
# Repository: https://github.com/Amey-Thakur/CRYPTOGRAPHY-AND-SYSTEM-SECURITY-AND-SYSTEM-SECURITY-LAB
# Date: 29/01/2021

"""
Theory:
Transposition Cipher is a cryptographic algorithm where the order of characters 
in the plaintext is rearranged to form the ciphertext. The actual characters 
are not changed, only their position.

This program demonstrates the Columnar Transposition technique, where the message
is written out in rows of a fixed length, and then read out column by column, 
typically according to a keyword.
"""

# Python3 implementation of Columnar Transposition 
import math 

key = "MEGA"

# Encryption 
def encryptMessage(msg): 
    """
    Encrypts the message using Columnar Transposition Cipher.
    
    Args:
        msg (str): The plaintext message.
        
    Returns:
        str: The encrypted ciphertext.
    """
    cipher = "" 

    # track key indices 
    k_indx = 0

    msg_len = float(len(msg)) 
    msg_lst = list(msg) 
    key_lst = sorted(list(key)) 

    # calculate column of the matrix 
    col = len(key) 
    
    # calculate maximum row of the matrix 
    row = int(math.ceil(msg_len / col)) 

    # add the padding character '_' in empty 
    # the empty cell of the matix 
    fill_null = int((row * col) - msg_len) 
    msg_lst.extend('_' * fill_null) 

    # create Matrix and insert message and 
    # padding characters row-wise 
    matrix = [msg_lst[i: i + col] 
            for i in range(0, len(msg_lst), col)] 

    # read matrix column-wise using key 
    for _ in range(col): 
        curr_idx = key.index(key_lst[k_indx]) 
        cipher += ''.join([row[curr_idx] 
                        for row in matrix]) 
        k_indx += 1

    return cipher 

# Decryption 
def decryptMessage(cipher): 
    """
    Decrypts the ciphertext using Columnar Transposition Cipher.
    
    Args:
        cipher (str): The encrypted ciphertext.
        
    Returns:
        str: The decrypted plaintext.
    """
    msg = "" 

    # track key indices 
    k_indx = 0

    # track msg indices 
    msg_indx = 0
    msg_len = float(len(cipher)) 
    msg_lst = list(cipher) 

    # calculate column of the matrix 
    col = len(key) 
    
    # calculate maximum row of the matrix 
    row = int(math.ceil(msg_len / col)) 

    # convert key into list and sort 
    # alphabetically so we can access 
    # each character by its alphabetical position. 
    key_lst = sorted(list(key)) 

    # create an empty matrix to 
    # store deciphered message 
    dec_cipher = [] 
    for _ in range(row): 
        dec_cipher += [[None] * col] 

    # Arrange the matrix column wise according 
    # to permutation order by adding into new matrix 
    for _ in range(col): 
        curr_idx = key.index(key_lst[k_indx]) 

        for j in range(row): 
            dec_cipher[j][curr_idx] = msg_lst[msg_indx] 
            msg_indx += 1
        k_indx += 1

    # convert decrypted msg matrix into a string 
    try: 
        msg = ''.join(sum(dec_cipher, [])) 
    except TypeError: 
        raise TypeError("This program cannot", 
                        "handle repeating words.") 

    null_count = msg.count('_') 

    if null_count > 0: 
        return msg[: -null_count] 

    return msg 

# Driver Code 
if __name__ == "__main__":
    msg = "Amey Thakur"
    print("Original Message: " + msg)

    cipher = encryptMessage(msg) 
    print("Encrypted Message: {}".format(cipher)) 

    print("Decryped Message: {}".format(decryptMessage(cipher))) 
 
