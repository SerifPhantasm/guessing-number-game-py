# tt
import random
import time

Yestxt = ["Yes", "yes", "ye", "Ye"]
Notxt = ["No", "no"]
IncorrectList = ["Incorrect!", "That is Incorrect!", "Try Again!", "Wrong number!", "Try Again...", "Nope.", "Incorrect!!!"]

## random.randrange(3, 9)

print("You need to give 2 numbers. You will guess a number between those two numbers.")
time.sleep(0.5)
print("The second number has to be bigger than the first number.")
time.sleep(0.5)
# first number
while True:
    try:
        AskUserforn1 = int(input("What's the first number? "))
        time.sleep(0.4)
        if AskUserforn1 == (int):
            break
        break
    except:
        print("Not a Number/Valid Number")
        continue
    

while True:
    # second number
    try:
        AskUserforn2 = int(input("What's the second number? "))
        if AskUserforn2 < AskUserforn1:
            print("The second number is too small, try a bigger number.")
            continue
        elif AskUserforn2 == AskUserforn1:
            print("It can't be the same numbers.")
            continue
        else:
            break
        
        
    except:
        print("Not a Number/Valid Number")



TheNumber = random.randrange(AskUserforn1, AskUserforn2)
time.sleep(0.2)
TheNumberInt = int(TheNumber)

while True:
    try:
        Answer1 = int(input("What is the number?"))

        if Answer1 < AskUserforn1:
            print("Not possible... Too low.")
            print("")
            time.sleep(0.1)
            continue
        elif Answer1 > AskUserforn2:
            print("Not possible... Too high.")
            print("")
            time.sleep(0.1)
            continue


        
        if (Answer1 == TheNumber):
            print("That is the correct Answer!")
            break
        else:
            print(random.choice(IncorrectList))
            print("")
            time.sleep(0.1)
            
            
    except:
        print("error")

print("The correct answer was:", TheNumberInt)
input("    ")

# This is the REAL guessing number game, where you have to guess the number 😱