'''
for operator
break and else operator
while operator
'''

print("======== for operator ========")
text = "aadi clothing brand"
numbers = [1, 8, 4, 45, 46, 77, 89]
car_obj = dict(brand="Lambarghine Uruse", origin="Northern Italy")

for letter in text:
    print(f"The letter of text: {letter}")

for n in numbers:
     print(f"The number of NUMBER list: {n}")

for key in car_obj:
     print(f"The key of car_obj: {key}, value of object: {car_obj.get(key)}")


#============================================================================================
print("======== break and else operator ========")

for n in numbers:
    print(f"The number of NUMBER list: {n}")
    if n > 45:
        print("Break work here because of condition")
        break
else:
        print("Loop worked without breaking")


#============================================================================================
print("======== while operator ========")
import random
compNum = random.randint(0, 100)

count = 0 
userNum = int(input("Enter Number "))

while compNum != userNum:
    
    count +=1
    if userNum < compNum:
            print(f"Nice try but {userNum} is False! HINT: it is higher than {userNum}")
            userNum = int(input("Enter number: "))

    elif  userNum > compNum:
            print(f"Nice try but {userNum} is False!, HINT: it is lower than {userNum}")
            userNum = int(input("Enter your number: "))

else:
        print(f"Wow, you find Correct number: {userNum} in {count} shots.")