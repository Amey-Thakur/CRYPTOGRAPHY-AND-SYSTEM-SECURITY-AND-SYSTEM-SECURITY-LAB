# Experiment 2: RSA & Digital Signature 
# Course: System Security Lab (CSL604)
# Name: Amey Thakur (https://github.com/Amey-Thakur)
# Roll No: 50
# Batch: B3
# Repository: https://github.com/Amey-Thakur/CRYPTOGRAPHY-AND-SYSTEM-SECURITY-AND-SYSTEM-SECURITY-LAB
# Date: 11/02/2021

"""
Theory:
RSA (Rivest–Shamir–Adleman) is a public-key cryptosystem that is widely used for secure data transmission.
It is based on the practical difficulty of the factorization of the product of two large prime numbers, 
the "factoring problem".

Key Generation:
1. Select two large prime numbers, p and q.
2. Calculate n = p * q. The public key is based on n.
3. Calculate the totient function, phi(n) = (p-1)(q-1).
4. Select an integer e such that 1 < e < phi(n) and gcd(e, phi(n)) = 1.
5. Calculate d such that d * e = 1 (mod phi(n)). d is the private key.

Encryption: c = m^e mod n
Decryption: m = c^d mod n
"""

def gcd(a, b):
    """
    Calculates the Greatest Common Divisor (GCD) of a and b recursively.
    Used to verify that 'e' and 'phi' are coprime.
    """
    if b == 0:
        return a
    return gcd(b, a % b)

def m_inv(e, n):
    """
    Calculates the Modular Multiplicative Inverse of e modulo n.
    Finds 'd' such that (d * e) % n == 1.
    This uses a brute-force approach for demonstration (for small numbers).
    For larger numbers, the Extended Euclidean Algorithm is preferred.
    """
    for d in range(1, n):
        if (e * d) % n == 1:
            return d
    return None

# Driver Code
if __name__ == "__main__":
    # 1. Input Prime Numbers
    p = int(input("Enter Value of p (Prime 1): "))
    q = int(input("Enter value of q (Prime 2): "))
    
    # 2. Input Public Exponent
    e = int(input("Enter value of e (Public Exponent): "))
    
    # 3. Calculate n (Modulus)
    n = p * q
    
    # 4. Calculate Euler's Totient Function phi(n)
    phi = (p - 1) * (q - 1)
    
    # 5. Verify that e is coprime to phi(n)
    if gcd(e, phi) != 1:
        print("Error: 'e' must be coprime to phi(n).")
        e = int(input('Enter different value for e: '))
    
    # 6. Calculate Private Key d
    d = m_inv(e, phi)
    
    print(f"\nPublic Key: (e={e}, n={n})")
    print(f"Private Key: (d={d}, n={n})")
    
    # 7. Input Message
    input_text = input("\nEnter Message to Encrypt: ")
    
    # 8. Encryption Process
    # Convert each character to its ASCII value, raise to power e, and mod n
    plaintext_ascii = [ord(char) for char in input_text]
    ciphertext_blocks = [(block ** e) % n for block in plaintext_ascii]
    
    # Formatting ciphertext for display (e.g., block#block#...)
    ciphertext_str = '#'.join(map(str, ciphertext_blocks))
    print('Encrypted Text: ' + ciphertext_str)
    
    # 9. Decryption Process
    # Take each cipher block, raise to power d, and mod n to recover ASCII value
    decrypted_ascii = [(block ** d) % n for block in ciphertext_blocks]
    decrypted_text = ''.join(map(chr, decrypted_ascii))
    
    print('Decrypted Text: ' + decrypted_text)
