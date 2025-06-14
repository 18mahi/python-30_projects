import random
import string

pass_len=int(input("enter password length: "))
charvalues=string.ascii_letters+string.digits+string.punctuation

#first method for generating password
#list comprehension [function for i in range(n)]
password="".join([random.choice(charvalues) for i in range(pass_len)])

#second method for generating password
'''password=""
for i in range(pass_len):
    password+=random.choice(charvalues)'''

print("your random password is:", password)