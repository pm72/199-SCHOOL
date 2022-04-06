# name = input("What is your name: ")
# print(f"Hello {name}!")
# greeting = f"Hello {name}! I am glad to see you!"

greeting = "Hello {}! I am glad to see you!"
message = "Your favorite number is {}"
#
# print(greeting.format(name))
#
# name = input("What is your name: ")
# print(greeting.format(name))
#
# number1 = input("Enter the first number: ")
# print(greeting.format(number1))

print(greeting.format(input("What is your name? ")))
print(message.format(input("Enter your favorite number: ")))