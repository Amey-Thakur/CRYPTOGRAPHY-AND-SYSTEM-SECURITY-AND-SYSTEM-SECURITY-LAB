def gcd(a, b):
	if b==0:
    		return a
	return gcd(b, a%b)
 
def m_inv(e, n):
	for _ in range(1,n):
    		if (e*_)%n == 1:
        		return _
 
 
p = int(input("Enter Value of p: "))
q = int(input("Enter value of q: "))
e = int(input("Enter value of e: "))
n = p*q
phi = (p-1)*(q-1)
 
if gcd(e, phi)!=1:
	e = int(input('Enter different value for e: '))
 
 
# e = 65537 #Fermat Number 2**2**4 + 1
 
d = m_inv(e, phi)
 
input_text = input("Message: ")
 
plaintext = ''
 
for _ in input_text:
	plaintext += str(ord(_))+'#'
 
 
 
plaintext = plaintext.split('#')[:-1]
 
 
ciphertext = ''
for _ in plaintext:
	ciphertext += str(int(_)**e % n)
	ciphertext += '#'
 
print('Encrypted Text: '+ciphertext)
 
decrypt = ''
 
ciphertext = ciphertext.split('#')[:-1]
 
for _ in ciphertext:
	decrypt += chr(int(_)**d % n)
  
print('Decrypted Text: '+decrypt)
