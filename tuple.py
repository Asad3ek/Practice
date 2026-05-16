'''
1. What is the Tuple?
2. Unpacing arguments
3. ZIP 

'''

print("======= What is the Tuple? =======")

#uple — bu: ordered va immutable collection. Ya’ni: elementlar tartibli saqlanadi lekin keyin o‘zgartirib bo‘lmaydi.
# PHP Java Nodejs dagi array tushunchasi = Pthyonda list tushunchasiga.

# Literal 
numbs = [1, 34, 76, 23, 7]

# constractor 
letter = list("aadi market")

fruits = ["Banana", "Melon", "Kivi", "Apple"]
print("before fruite list:", fruits)

fruits[1] = "Lemon"
print("after fruite list:", fruits)

# tuple ichida yozilgan itemlarni o'zgartirib bo'lmaydi.
car = ("BMW", "LAMBARGHINE", "PORSCHE", "CADELLAC ESCALETE")

#car[1] = "G wagon"
print("car", car)

# 'tuple' object does not support item assignment ko'rinishidagi error chiqadi.


print("======= Unpacing arguments =======")

car = ["BMW", "LAMBARGHINE", "PORSCHE", "CADELLAC ESCALETE"]

(a, b, c, d) = car
print(f"a: {a} b: {b} ")

#============================
(a, b, *c) = car
print(f" c: {c}")

# *args => tuple 

def calculate(*args):
    print("args : ", args)
    total = 2
    for x in args:
        total *= x 
    print(f"total value: {total}")
    return total 
    
calculate(2, 3, 4, 6)
calculate(22, 3, 4, 5)

def greeting(*args, **kwargs):
    print("*args : ", args)
    print("**kwargs : ", kwargs)

greeting("hello", 10, True, name="Anthony", age=25)

print("======= ZIP =======")

tuple1 = (1, 5, 7, 3, 9)
tuplpe2 = ("a", "b", "y", "u")
zipped = zip(tuple1, tuplpe2)

result = list(zipped)
print("ZIpped Result: ", result)

