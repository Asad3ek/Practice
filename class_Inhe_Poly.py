'''
What is the Encapsulation?
What is the INHERITANCE?
WHAT IS THE POLYMORPHYSIM?

'''

print("======== What is the Encapsulation?========")
# Encapsulation bu - data hamda logic ni capsulaga solib tashqi access larni control qiladi va data secure qiladi
#In PYTHON:
# public - o'zi yoziladi
# __Private - __ bn soziladi
# _Protect - bitta _ bn yoziladi.


print("======== What is the INHERITANCE? ========")
#Inheritance - bu parent classdan child classlar state hamda methodlarini meros olishiga ayatiladi

class Animal():
    #state
    description = "The class is parent for Animals"

    #constraction 
    def __init__(self, sound, voice):
       
        self.sound = sound 
        self.voice = voice

    #method 
    def make_noise(self):
        print(f"This Animal make voice: {self.voice} and sound: {self.sound}")


class wolf(Animal):

    def __init__(self, name, sound, voice):
        self.name = name
        super().__init__(sound, voice)

    def introduce(self):
        print(f"The name of Wolf is white {self.name}")


class sheep(Animal):

    def __init__(self, name, sound, voice):
        self.name = name
        super().__init__(sound, voice)

    def introduce(self):
        print(f"The name of Sheep is {self.name}")


new_wolf = wolf("Balto", "auuuuv", True)
new_sheep = sheep("Baran", "Baaaa", True)
new_wolf.introduce()
new_wolf.make_noise()

new_sheep.introduce()
new_sheep.make_noise()
print(Animal.description)


print("====== WHAT IS THE POLYMORPHYSIM? ======")

'''Polymorphism nima?
Polymorphism — OOP dagi prinsip bolib, manosi:

Bir xil interface yoki method,
har xil objectlarda har xil ishlashi

“Poly”: >> kop

“Morphism”: >> shakl

Demak: >> “One interface, many forms”

'''
        