print("====== Operators ======")

a = 10
b = 5

print(a / b)
print(a * b)
print(a + b)

print(a // b) # butun qismini qaytaradi
print(a % b) #qoldiq qismini qaytaradi.
print(a **2) # kvadrarini qaytaradi
print(a **3) # kubini yani 3 darajasini qaytaradi




print("====== Logical operators ======")


age = 20 

person = None

if age > 18:
    person = "Adult" 
else:
    person = "Minor"

print("Person:", person)

person2 = "Adult" if age > 18 else "Minor"
print("Person2:", person2)