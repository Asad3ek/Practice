'''Packages and debugging:
1. Python packages & core packages
2. ackages manager & External packages
3. Debugging
'''

from PIL import Image
import turtle
print("====== Python packages & core packages =====")
# core Packages

# t = turtle.Turtle()
# t.shape("turtle")
# t.speed(2)
# t.circle(200)
# turtle.done()

my_file = open("materials/messages.txt", "r")
try:
    content = my_file.read()
    print("content:", content)
finally:
    my_file.close()
print("$===$"*10)
# with - context manager
with open("materials/messages.txt", "r") as your_file:
    your_content = your_file.read()
    print("your_content: ", your_content)
    print("it worked as past")

print("====== Packages manager & External packages =====")
# "Python External pacage link: https://pypi.org "
'''
pillow - working with images 
moment - time packages
'''

with Image.open("materials/image1.png") as img:
    resized_img = img.resize((200, 400))
    resized_img.show()
    resized_img.save("materials/images.png")


print("====== Debugging =====")


def function(*args):
    total_amount = 0
    for a in args:
        total_amount += a
    return total_amount  # solve bug via debugging


result = function(1, 4, 7, 9, 3, 5, 2, 8, 6)
print("RESULT: ", result)
