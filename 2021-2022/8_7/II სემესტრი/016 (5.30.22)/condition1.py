# პირობითი ოპერატორები

# bool  True/False
# a = True
# b = False
# print(f"a is {a} & b is {b}")
# print(f"a is {int(a)} & b is {int(b)}")

# print(bool(0), bool(0.0), bool(""), bool(None))
# print(bool(58), bool(-84), bool(1.24), bool(" "), bool("Paata"))

# შედარების ოპერატორები > < >= <= == !=
# a = 5
# b = 12
# print(a < b)  # True
# print(a > b)  # False
# print(a <= b)  # True
# print(a >= b)  # False
# print(a == b)  # False
# print(a != b)  # True

# if, if .. else, if .. elif .. .. else
# age = int(input("Age: "))
# if age <= 5:
#   print("You are a little kid ☺☻")

try:
  age = int(input("Age: "))
  if age <= 0:
    print("Please, Enter positive number!")
    print("\nDone!")
    exit()
  elif age <= 5:
    print("You are a little kid ☺☻")
  elif age <= 12:
    print("You are a big kid ☺☻")
  elif age <= 19:
    print("You are a Teenager ☺☻")
  elif age >= 20:
    print("You are an adult already ♥")
except ValueError:
    print("Not an integer number. Please, re-run the program.")
    print("\nDone!")
    exit()


print("\nDone!")