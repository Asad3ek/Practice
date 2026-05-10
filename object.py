'''OBJECT
    1. What is Object?
    2. Iterable objects and Range
    3. Dictionary 
    4. Error Handling system
'''

print("====What is the Object?====")
#An Object has method and state properties
#Everything is object in Python.

'''Import qilishi shart bo'lgan Module/Package lar in Python:

    1. Math >> 2. Array >> 3. os >> 4. sys >> 5. random >> 6. datetime >> 7. json >> 8. re
    9. numpy >> 10. pandas >> 11. matplotlib >> 12. opencv >> 13. sklearn >> 14. torch
'''

import array
import math
from math import asin
#Paradigmas >> Functional & OOP paradigmas
# OOP >> 4 consepts:
# 1. Abstraction >> 2. Encapsulation >> 3. Inheritence >> 4. Poliymorphysm. 
a = 101.29
b = 0.88
result1 = math.ceil(a)
print("NATIJA1:", result1)


result2 = asin(b)
print("NATIJA2:", result2)


print("==== Iterable objects and Range ====")
# Iteration — object ichidagi elementlarni navbat bilan ko‘rib chiqish jarayoni.
# iteration obj: String / dictionary / tuple / list / range / map / filter.

text =  "Porsche Tycane"
for letter in text:
    print(f"The letter:", letter)

range_obj = range(7)
for ele in range_obj:
    print(f"The number: {ele}")


print("==== DICTIONARY ====")
# DICTIONARY has become common as a Json object in Python. 
# object qurish:

car = {"Brand": "Porsche", "Model": "Tycane", "Year": "2026"}
person_obj = dict( name="Khalid", Age=20, Job="Student")

print(f"Car features: {car}")
print(f"Person Introduce: {person_obj}")

name = person_obj.get("name")
person_balance = person_obj.get("balance", 0)
print("PERSON name: ", name)
print("PERSON Balance: ", person_balance)


# key yoki value ni delete qilish uchun method 
del person_obj["name"]

for key in person_obj:
    print(f"key: {key}, value: {person_obj.get(key)}")

for key in car:
    print(f"key: {key}, value: {car.get(key)}")


print("==== Error Handling system ====")

food_obj = dict(type="Healthy",name="Plov", calories=500)



try:
    a = food_obj.prepare
    food_org = food_obj["origin"] 
    print("food_org:", food_org)
except KeyError as err:
    print("food_obj has not: ", err, "state")
except AttributeError as err:
    print("food_obj could not find: ", err)
else: 
    print("Executed successfully without ERROR")
finally: 
    print("Final logic") 

    # exption error bu general error ni handle qilish hisoblanadi. 
# except Exception as err:
