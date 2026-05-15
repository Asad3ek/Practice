import random 
compNum = random.randint(0, 100)

def findNumber(compNum):
    userNum = int(input("Enter number: "))
    step = 1

    while compNum != userNum:
        step += 1
        if userNum < compNum:
            print(f"Nice try but {userNum} is False! HINT: it is higher than {userNum}")
            userNum = int(input("Enter number: "))

        elif  userNum > compNum:
            print(f"Nice try but {userNum} is False!, HINT: it is lower than {userNum}")
            userNum = int(input("Enter your number: "))

    else:
            print(f"Wow, you find Correct number: {userNum} in {step} shots.")

    

findNumber(compNum)
