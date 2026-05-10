print("=========Primitive Variables=========")
''' String
    Number
    Boolean 
    Null
    Undefined
'''
# VARIABLES in JavaScript  - name of the storage location deyiladi

# VARIABLES In Python - name of the reference!
# yani hamma narsa obj bo'lganligi sababli reference ning nomlanishi deyiladi.

print("====Number variables====")

count = 47
count_type = type(count)
print(f"The count: {count}, The type of count: {count_type}")


print("====String variables====")
course = "AI PYTHON fullstack "
result = type(course)
result1 = course.title()
print(f"Course Title: {result1}, The type of course title: {result}")
   
result = course.replace("AI", "Artificial Intellegence").upper()
print(result)

# bu method lar boshlang'ich kiritilgan datani saqlagan holda o'zgartiradi


print("====Boolean variables====")
# function > input(), str(), bool(), int()
Z = input("Enter your value for Z ")
print("Z:", Z)

result = Z.isnumeric()
print(f"The Input Value is Numeric: {result}")

# TRUTHY >> true,  " ", number(100), string(abc)
# FALTHY >> 0, "", false, none


test_falsy = ""
result1 = bool(test_falsy)
print("result1:", result1)

test_truthy = 100
result2 = bool(test_truthy)
print("result2:", result2)
