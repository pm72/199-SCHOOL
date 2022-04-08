from random import uniform

message1 = "Welcome {}!"
message2 = "{}, your age is {}!   you are teen!"

name = input("Enter your name: ")
age = input("Please, enter your age: ")
print(f"{message1.format(name)}\n{message2.format(name, age)}")

print("# =================")
print("# =================")
print("# =================")
print("# =================\n")

name = input("Enter your name: ")
age = input("Please, enter your age: ")
print(f"{message1.format(name)}\n{message2.format(name, age)}")

print("# =================")
print("# =================")
print("# =================")
print("# =================\n")

text = input("Text: ")
print(f"{message1.format(text)}\n{message2.format('text', uniform(0.56, 1.89))}")