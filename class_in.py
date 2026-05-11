'''CLASS

1. What is the class?
2. Ordinary & Static Properties
3. Special Methods

'''
print("===>> What is the class? <<===")

# class is a template to create objects and class consist of 3 part:
# 1. State
# 2. Constructor 
# 3. Method

class Person():
    # 1. State
    message = "State properties of Class"

  # 2. Constructor 
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

    # 3. Method
    def intraduce(self):
        print(f"{self.name}: Hello! My name is {self.name}, and I live in {self.country}.")

    def say_age(self):
        print(f"{self.name}: By the way I am {self.age}. years old.")

    def intraduceFull(self):
        print(f"{self.name}: Hello! My name is {self.name}, and I live in {self.country}. I am {self.age}. years old.")

    @classmethod
    def explane(cls):
        print("The Static Method Properties Executed.")


person1 = Person("Anthony", 25, "Uzbekistan")
person2 = Person("Khalid", 20, "United Arab Emitrates")
person3 = Person("Leyla", 19, "Turkey")


print("===>> Ordinary & Static Properties <<===")

#ordinery method 
person1.intraduce()
person2.say_age()
person3.intraduceFull()

# static method
new_message = Person.message
print("NEW MESSAGE: ", new_message)

Person.explane()


print("===>> Special Methods <<===")

class Car():
    # state
    description = "this class makes car"

    def __new__(cls, *args):
        print("$ >> __new__ << $")
        return super().__new__(cls)
    
    # constructor
    def __init__(self, name, year, origin):
        self.name = name
        self.year = year
        self.origin = origin

    # method
    def startEngine (self):
        print(f"The {self.name} started Engine!")

    def stopEngine(self):
        print(f"The {self.name} stopped Engine!")

    def __str__(self):
        return f"The {self.name} vehicle Prodused in the {self.origin} at {self.year} years!"
    
    def __call__(self, *args, **kwds):
        print("Call Special Method helping OBJ to call as a function")
        return True

myCar = Car("Porsche", 2026, "Germany")
myCar2 = Car("Mercedes-Benz G-Wagon ", 2027, "Germany")

    
myCar.startEngine()
myCar2.stopEngine()

your_car = Car("BMW", 2026, "Germany")
print(your_car)

result = myCar2() # calling as a function >> we need __call__ special method
print("Responce: ", result)


