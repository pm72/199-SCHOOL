message1 = "Welcome {}!"
message2 = "{}, your favorite numner is {}"

name = input("Name: ")
number = input("Favorite number: ")

print(f"{message1.format(name)}\n{message2.format(name, number)}")


# =====================
# =====================
# =====================
# =====================
# =====================

print("\n")

name = input("Name: ")
number = input("Favorite number: ")

print(f"{message1.format(name)}\n{message2.format(name, number)}")