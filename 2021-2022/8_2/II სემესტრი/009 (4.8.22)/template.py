from random import uniform

greeting = "Welcome {}!"
message = "{}, your favorite number is {}"

name = input("Enter your name: ")
number = input("Enter your favorite number: ")

print(greeting.format(name))
print(message.format(name, number))

print("\n# =================")
print("# =================")
print("# =================")
print("# =================\n")

name = input("Enter your name: ")
number = input("Enter your favorite number: ")

print(greeting.format(name))
print(message.format(name, number))

print("\n# =================")
print("# =================")
print("# =================")
print("# =================\n")

print(greeting.format("Maka"))
print(message.format("Nino", uniform(0.56, 0.89)))