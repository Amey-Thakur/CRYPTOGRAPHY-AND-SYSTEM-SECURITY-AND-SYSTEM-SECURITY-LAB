import hashlib

# initializing string 
str1 = "MEGA"
str2 = "ARCHIT"
str3 = "SAAKSHI"
# then sending to md5() 
result1 = hashlib.md5(str1.encode())
result2 = hashlib.md5(str2.encode())
result3 = hashlib.md5(str3.encode())

# printing the equivalent hexadecimal value. 
print("The hexadecimal equivalent of hash is : ", end ="") 
print(result1.hexdigest())
print(result2.hexdigest())
print(result3.hexdigest())
result1 = int(str1, 32)
result2 = int(str2, 32)
result3 = int(str3, 32)

print("The decimal number of hexadecimal string : " + str(result1))
print("The decimal number of hexadecimal string : " + str(result2))
print("The decimal number of hexadecimal string : " + str(result3))
diff1=result2-result1
diff2=result3-result2
print(" ")
print("The key difference between result 1 and 2 : " + str(diff1))
print("The key difference between result 2 and 3 : " + str(diff2))
