from random import uniform as un

message1 = "Welcome {}!"
message2 = "{}, your entered favorite number is {}."

name = input("Name: ")
number = input("Number: ")

print(f"{message1.format(name)}\n{message2.format(name, number)}")

print("# =====================")
print("# =====================")
print("# =====================")
print("# =====================\n")

name = input("Name: ")
number = input("Number: ")

print(f"{message1.format(name)}\n{message2.format(name, number)}")

print("# =====================")
print("# =====================")
print("# =====================")
print("# =====================\n")

text = input("Text: ")

print(f"{message1.format(text)}\n{message2.format(name, un(0.58, 1.56))}")