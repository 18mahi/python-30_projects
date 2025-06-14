import random

computer=random.randint(-1,1)
user=int(input("enter snake for -1, water for 0, gun for 1: "))
print("computer generate:",computer)
if(computer==-1):
    if(user==-1):
        print("--DRAW--")
    elif(user==0):
        print("--LOOSE--")
    else:
        print("--WIN--")
elif(computer==0):
    if(user==-1):
        print("--WIN--")
    elif(user==0):
        print("--DRAW--")
    else:
        print("--LOOSE--")
else:
    if(user==-1):
        print("--LOOSE--")
    elif(user==0):
        print("--WIN-- ")
    else:
        print("--DRAW--")
    