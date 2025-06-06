import random

target=random.randint(1,100)
print("Welcome to the number guessing game!")
print("you have 5 chances to guess the number between 1 and 100.")
i=1
while (i<=5):
    userchoice=input("guess the target: OR Quit: ")
    if(userchoice=="Quit"):
        break
    userchoice=int(userchoice)
    if(userchoice==target):
        print("success: correct guess!")
        break
    elif(userchoice<target):
        print("your number was too small. Take a bigger guess...")
    else:
        print("your number was too big. Take a smaller guess...")
    i+=1
if(i>5):
    print("You have exhausted all your chances.")
    print("The target number was:", target)
else:
    print("You guessed the number in", i, "tries.")
print("Thank you for playing!")
print("---GAME OVER----")