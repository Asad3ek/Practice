'''
1. working with Lists
2. List methods
3. Lambda function
'''

print("======= working with Lists =======")


#Literal way 
numbs = [1, 45, 65, 3, 7, 9] # list
fruits = ("Banana", "Melon", "Kivi", "Apple") #tuple
person = {"name" : "Anthony", "age" : 25} # dictionary 

for meva in fruits:
    print(f"meva: {meva}")

#constructor way 
letter = list("aadi market")
print(f"letter: {letter} and size: {len(letter)}")

# =======================================================
fruits = ("Banana", "Melon", "Kivi", "Apple")

a = fruits[0]
b = fruits[0:2] # 0 dan 2gacha 2 kirmaydi value ni oladi yani [0:2)
c = fruits[::3] # birinchi keyni va ikkita sakirab 3 keyni oliub ber degani
d = fruits[::-1] # listni teskariga o'giradi 

print("A :", a)
print("B :", b)
print("C :", c)
print("D :", d)

print("======= List methods =======")
# Methods => append() insert() pop() remove() clear() sort() => mutable | index() => immutable
letters = ["a", "s", "f", "r", "e"]

letters.append("aadi") # add behind | end of the list
print(f"Letter append: {letters}")

letters.insert(0, "MIT") # add front of list 
print(f"Letter insert: {letters}")

size = len(letters) -1
result = letters.pop(size) #pop behind
print(f"result pop: {result} and letter: {letters}")
result2 = letters.pop(0) # pop front 
print(f"result2 pop: {result2} and letter: {letters}")


# =======================================================
car = ["BMW", "Porsche", "Mercedes", "Uzdaewoo", "GM", "Toyota", "Lambarghine"]
print("car list: ", car)

car.remove("GM")
print("car remove: ", car) # remove method

del car[3:5]
print("car delete: ", car)


exist = car.index("BMW") # index method
print("car exist:", exist)

car.clear()
print("car clear:", car)

if "BMW" in car:
    print(f"index of BMW: {car.index("BMW")}")
else:
    print("BMW is not exist in Car list")


numbs = [1, 45, 65, 3, 7, 9] # list
numbs.sort()
print("DEFAULT Sorted list of Numbs: ", numbs) #kichikdan kattaga qarab 

numbs.sort(reverse=True)
print("REVERSE Sorted list of Numbs: ", numbs) # kattadan kichikka qarab

numbers = [23, 45, 1 , 67, 35 , 23, 5]
print("NUMBER: list: ", numbers)

new_numb = sorted(numbers)
print("New NUMBER list: ", new_numb)


print("======= Lambda function =======")

people = [
    ("Anthony", 25),
    ("Daminic", 23),
    ("Sunaya", 22),
    ("Khalid", 10),
    ("Zubayr", 12)
]
people.sort()
print("people1", people)
people.sort(key=lambda person: person[1])
print("people2 ", people) # sorted via lambda function

print("======= Enumerate | filter | map =======")

animal = ["wolf", "Lion", "Horse", "Geopart"]
for element in enumerate(animal):
    print("element: ", element)

for (index, value) in enumerate(animal):
    print(f"element index:{index} and element value: {value}")

car_obj = dict(brand="BMW", year=2025, brand2="Lambarghine", year2=2026)
result = car_obj.items()
for (key, value) in result:
    print(f"the key: {key} ")
    print(f"the value: {value} ")