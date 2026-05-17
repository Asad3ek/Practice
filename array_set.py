'''Array & set
1. Array 
2. Set

'''

print("======= ARRAY =====")
from array import array 
numbers = array("i", [23, 3, 67, 83, 4, 68, 89, 0])
print("Numbers list1: ", numbers)

numbers.append(7)
numbers.insert(3, 47)
numbers.remove(89)
print("Numbers list2: ", numbers)

del numbers[1::6]
print("Numbers list3: ", numbers)

print("======= Set =====")
# { SET } - bu arraydafi bir xil bo'lgan malumotlarning faqat bittasini oladi.
database = array("i", [12, 3, 4, 2, 3, 14, 7, 8, 3, 45, 5, 23, 34, 34 ,6 ,76, 78, 7, 77, 75, 4, 36, 7, 7, 3, 6, 54])
print("Database1:", database)
new_database = set(database)
print("Database2:", new_database)
# set listi ichiga mavjud bo'lmagan sonni inser() yoki add() qilsak listga qabul qiladi ammo mavjud sonni qabul qilmaydi


print("======= Spesific operators with Set =====")
# | & - ^
numb1 = {77, 45 , 7, 14, 77}
numb2 = {77, 45 , 10, 11}

result1 = numb1 | numb2       #ikkita setni bitta qilib beradi takrorlashlarsiz => result1: {7, 10, 11, 45, 77, 14}
print("result1:", result1)

result2 = numb1 & numb2
print("result2:", result2)   #ikkita setda mavjud bir xil sonlarni olib beradi => result2: {77, 45}

result3 = numb1 ^ numb2
print("result3:", result3)   #ikkita setda ham mavjud bo'lgan sonlarni tashlab yuboradi qolganlarni bitta arrayda 
                             #set qilib beradi => result3: {7, 10, 11, 14}
