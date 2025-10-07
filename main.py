# tt
import random
import time

Yestxt = ["Yes", "yes", "ye", "Ye"]
Notxt = ["No", "no"]
IncorrectList = ["Incorrect!", "That is Incorrect!", "Try Again!"]

## random.randrange(3, 9)

print("You need to give 2 numbers. You will guess a number between those two numbers.")
time.sleep(0.5)
AskUserforn1 = int(input("What's the first number?"))
time.sleep(0.4)
AskUserforn2 = int(input("What's the second number?"))

TheNumber = random.randrange(AskUserforn1, AskUserforn2)
TheNumberInt = int(TheNumber)

while True:
    try:
        Answer1 = int(input("What is the number?"))

        if (Answer1 == TheNumber):
            print("That is the correct Answer!")
            break
        else:
            print(random.choice(IncorrectList))
            
            
    except:
        print("error")

print("The correct answer was:", TheNumberInt)
input(".    ")