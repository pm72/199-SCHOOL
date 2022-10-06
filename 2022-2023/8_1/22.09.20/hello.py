name = input("Enter your name: ")
age = eval(input("Enter your age: "))

print("Info:")
print(f"Name: {name}\nAge: {age}")
print(type(name), type(age))

print(f"{name}, after 10 years you will be {age + 10} years")

input()
