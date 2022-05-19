# ლოგიკური გამოსახულებები, ლოგიკური მნიშვნელობები True / False

# a = True
# b = False
# print(f"a is {a} & b is {b}")
# print(f"a is {int(a)} & b is {int(b)}")
# print(f"a is {float(a)} & b is {float(b)}")
#
# print()
#
# print(bool(1), bool(0))
# print(bool('Hello there!'))
# print(bool([89, 25]))
# print(bool([]))
# print(bool(''))
# print(bool(' '))
# print(bool(None))


# =====> ლოგიკური ოპერაციები <=====
# < > <= >= == !=
# print(2 < 3)  # True
# print(2 > 3)  # False

# a = 5 == 5
# b = 2 != 2
# c = 3 >= 5
# d = 5 <= 15
# e = 3 >= 3
# print(a, b, c, d, e)


# =====> განშტორბის ოპერატორი if <======
# if comparition:
#   lines of code

# age = int(input("What is your age? "))
# if age <= 5:
#   print("You are a little kid ☺☻")

# =====> ბლოკი else <======
# if .. else კონსტრუქცია
# age = int(input("What is your age? "))
# if age <= 5:
#   print("You are a little kid! ☺☻")
# else:
#   print("You are a big kid! ☺☻")


# =====> ბლოკი elif <======
# if .. elif .. else კონსტრუქცია
age = int(input("What is your age? "))
if age <= 5:
  print("You are a little kid! ☺☻")
elif age <= 12:
  print("You are a big kid! ☺☻")
elif age <= 19:
  print("You are teenager! ☺☻")
elif age >= 20:
  print("Wow, you are an adult already! ☺☻")
else:
  print("You hav't entered a number. Please re-run the program!")