# a = True
# b = False
#
# print(f"a is {a} & b is {b}")
# print(f"a is {int(a)} & b is {int(b)}")
#
# print()
#
# print(bool(1))
# print(bool(0))
# print(bool("Hi there!"))
# print(bool(""))
# print(bool(None))

# > < >= <= == !=
# print(3 > 5)
# print(3 < 5)
# print(3 == 3)
# print(2 != 2)
# print("hello" == "Hello")
# print("hello" == "hello")
# print(2 <= 2)
# print(3 >= 3)
# print(3 >= 5)

# =====> if <=====
# if comparison:
#   lines of code
# age = int(input("What is your age? "))
# if age <= 5:
#   print("You are a little kid :)")

# =====> else <=====
# else:
#   inner lines of code
# age = int(input("What is your age? "))
# if age <= 5:
#   print("You are a little kid :)")
# else:
#   print("You are a big kid ☺")

# =====> elif <=====
# elif condition:
#   inner lines of code
age = int(input("What is your age? "))
if age <= 5:
  print("You are a little kid ☺")
elif age <= 12:
  print("You are a big kid ☺")
elif age <= 19:
  print("You are a teenager! ☺")
elif age >= 20:
  print("Wow, you are an adult already!")
else:
  print("Looks like you've not entered a number. Please re-run the program.")