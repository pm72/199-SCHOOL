greeting = "Welcome {}!"
message = "{}, Your favorite number is {}."

name = input("What is your name? ")
number = input("Please, enter your favorite number: ")

print(greeting.format(name))
print(message.format(name, number))