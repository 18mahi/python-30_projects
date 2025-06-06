#perform operation on two numbers 
a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
operator=input("enter the arithmetic operator(+,-,*,/,%): ")
if (operator=="+"):
    result =a+b
elif (operator=="-"):
    result=a-b
elif(operator=="*"):
    result=a*b
elif(operator=="/"):
    result=a/b
elif(operator=="%"):
    result=a%b
else:
    print("invalid operator. please use +/-/*// or %")
    
print(result)