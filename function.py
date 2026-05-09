'''FUNCTIONS
Define & Call
parametr & argument 
keyword & default arguments
Scope
'''

# Reusable block of code - malum bir vazifani bajaradigan code block
# instead of block {} in JavaScript, Python uses Indentation!

# built in functions - bular bizga qurib berilgan functionlar xisoblanadi
# Bularga >> type(), print()... kabi functionlar misol bo'ladi


# DEFINE -- Parametr
def greet(name):
    print(f"How are you {name}!")


# CALL -- Argument
greet("Anthony")

print("==============keyword & default arguments===============")

# DEFINE


def greet(name, age):
    print("greet is executed")
    return f"Hello! My name is {name}, and I am {age} yeras old"


# CALL
result1 = greet("Tom Hardy", 45)
print("Natija:", result1)

# keyword argumets >>
result1 = greet(name="Tom Hardy", age=45)
print("Natija:", result1)
# keyword argumets kodimiz boshqalarga tushunarli bo'lishi uchun foydalanamiz

# default arguments
# default argumet - define qismidagi paramatrga kiritiladi va agar call qismida
# argumetn berish shart bo'lmaydi yoki berilmasa define qismidan olib ketadi.


def greet(name, age=44):
    print("greet is executed")
    return f"Hello! My name is {name}, and I am {age} yeras old"


# CALL
result1 = greet("Tom Hardy")
print("Natija:", result1)


print("==============SCOPE===============")
'''
Pythonda scope — o‘zgaruvchi (variable) qayerda “ko‘rinishi” va qayerdan unga murojaat qilish mumkinligini bildiradi.

Oddiy qilib: Variable qayerda yaratilgan bo‘lsa, o‘sha hudud uning scope’i
'''

b = 200


def calculate(a, b):
    c = a + b * a
    print(f"Value of C: {c}")


calculate(7, 47)

# SEARCHING: Local function ichidan → parametr dan
# → Function Tashqarisidan
# → Global
# → Built-in
