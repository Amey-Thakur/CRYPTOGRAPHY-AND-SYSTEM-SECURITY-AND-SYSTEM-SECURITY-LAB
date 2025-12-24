key = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(n, plaintext):
    result = ''

    for l in plaintext.lower():
        try:
            i = (key.index(l) + n) % 26
            result += key[i]
        except ValueError:
            result += l

    return result.lower()

def decrypt(n, ciphertext):
    result = ''

    for l in ciphertext:
        try:
            i = (key.index(l) - n) % 26
            result += key[i]
        except ValueError:
            result += l

    return result



text=input(str("Enter a message for Encryption: "))
print("Enter a Key: ")
offset=input()
offset=int(offset,10)

print ("Plaintext: " + text)
encrypted = encrypt(offset, text)
print('Encrypted Message: ', encrypted)

decrypted = decrypt(offset, encrypted)
print('Decrypted Message: ', decrypted)
