# Experiment 2: RSA Algorithm and Digital Signature (Mathematical Foundations)
# Course: System Security Lab (CSL604)
# Name: Amey Thakur (https://github.com/Amey-Thakur)
# Roll No: 50
# Batch: B3
# Repository: https://github.com/Amey-Thakur/CRYPTOGRAPHY-AND-SYSTEM-SECURITY-AND-SYSTEM-SECURITY-LAB
# Date: 11/02/2021

"""
Theory:
The RSA algorithm relies heavily on Number Theory, specifically:
1. Prime Numbers: Numbers divisible only by 1 and themselves.
2. Greatest Common Divisor (GCD): The largest positive integer that divides two numbers without a remainder.
3. Modular Arithmetic: Arithmetic for integers, where numbers "wrap around" upon reaching a certain value (modulus).
4. Euler's Totient Function phi(n): Counts the positive integers less than or equal to n that are relatively prime to n.
5. Modular Multiplicative Inverse: An integer d such that (d * e) % phi(n) = 1.
"""

def gcd(a, b):
    """
    Calculates the Greatest Common Divisor (GCD) of a and b using the Euclidean Algorithm.
    The algorithm proceeds in steps where in each step a is replaced by b and b by a % b,
    until b becomes 0.
    """
    if b == 0:
        return a
    return gcd(b, a % b)

def m_inv(e, n):
    """
    Calculates the Modular Multiplicative Inverse of e modulo n.
    This function finds an integer d such that (d * e) ≡ 1 (mod n).
    
    In RSA, 'd' is the Private Key exponent.
    It satisfies the congruence: d * e = 1 + k * phi(n) for some integer k.
    """
    for d in range(1, n):
        if (e * d) % n == 1:
            return d
    return None

# Driver Code
if __name__ == "__main__":
    print("--- RSA Mathematical Components Demonstration ---")
    
    # 1. Input Prime Numbers
    p = int(input("Enter Value of p (Prime 1): "))
    q = int(input("Enter value of q (Prime 2): "))
    
    # 2. Input Public Exponent
    e = int(input("Enter value of e (Public Exponent): "))
    
    # 3. Calculate n and phi
    n = p * q
    phi = (p - 1) * (q - 1)
    
    print(f"\nCalculated n: {n}")
    print(f"Calculated phi(n): {phi}")
    
    # 4. Verify Coprimality
    if gcd(e, phi) != 1:
        print("\nError: 'e' is not coprime to phi(n).")
        print(f"GCD({e}, {phi}) = {gcd(e, phi)}")
        e = int(input('Enter different value for e: '))
    
    # 5. Calculate Scalar d (Private Key)
    d = m_inv(e, phi)
    print(f"Calculated Private Key d: {d}")
    
    # 6. RSA Operation Demonstration
    input_text = input("\nMessage to Encrypt: ")
    
    plaintext = ''
    # Convert string to ASCII block representation
    for char in input_text:
        plaintext += str(ord(char)) + '#'
    
    plaintext_blocks = plaintext.split('#')[:-1]
    
    ciphertext = ''
    # Encryption: m^e mod n
    for block in plaintext_blocks:
        ciphertext += str(int(block) ** e % n)
        ciphertext += '#'
    
    print('Encrypted Text: ' + ciphertext)
    
    decrypt_text = ''
    # Decryption: c^d mod n
    ciphertext_blocks = ciphertext.split('#')[:-1]
    
    for block in ciphertext_blocks:
        decrypt_text += chr(int(block) ** d % n)
      
    print('Decrypted Text: ' + decrypt_text)
