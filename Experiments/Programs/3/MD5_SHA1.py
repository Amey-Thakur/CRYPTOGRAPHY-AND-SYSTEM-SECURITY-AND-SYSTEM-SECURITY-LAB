import hashlib

print("Message : AMEY")

result = hashlib.md5(b"AMEY").hexdigest()

result = hashlib.md5("AMEY".encode("utf-8")).hexdigest()

m = hashlib.md5(b"AMEY")

print("Hash Algorithm : ",m.name)
print("Digest Size (in bytes) : ",m.digest_size) 
print("Bytes : ",m.digest())    # bytes
print("Bytes in hex representation : ",m.hexdigest()) # bytes in hex representation

result = hashlib.sha1(b"AMEY").hexdigest()

result = hashlib.sha1("AMEY".encode("utf-8")).hexdigest()

m = hashlib.sha1(b"AMEY")

print("Hash Algorithm : ",m.name)
print("Digest Size (in bytes) : ",m.digest_size) 
print("Bytes : ",m.digest())    # bytes
print("Bytes in hex representation : ",m.hexdigest()) # bytes in hex representation
