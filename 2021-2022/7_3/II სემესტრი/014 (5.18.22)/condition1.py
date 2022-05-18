# =====> True / False <=====
# bool ტიპი

# a = True
# b = False
# print(f"a is {a} & b is {b}")
# print(f"a is {int(a)} & b is {int(b)}")
# print(f"a is {float(a)} & b is {float(b)}")
#
# print()
#
# print(bool(1))
# print(bool(-1))
# print(bool(0))
# print(bool("Hello there!"))
# print(bool(" "))
# print(bool(""))
# print(bool(None))

# =====> შედარების ოპერაციები და ოპერატორები <=====
# > < >= <= == !=
# print(3 > 5)
# print(3 < 5)
# print(3 == 3)
# print(2 != 2)
# print("hello" == "Hello")
# print("hello" == "hello")
# print("abcd" > "abd")
# print(3 >= 5)
# print(2 <= 5)
# print(5 <= 5)
# print(5 >= 5)

# =====> if <=====
# if condition:
#   lines of code
# age = int(input("What is your age? "))
# if age <= 5:
#   print("You ara a little kid ☺")    # smile  ===>  alt+numpad1

# =====> else <=====
# else:
#   lines of code
# age = int(input("What is your age? "))
# if age <= 5:
#   print("You ara a little kid! ☺")
# else:
#   print("You are a big kid! ☺")

# =====> else <=====
# elif condition:
#   lines of code
age = int(input("What is your age? "))
if age <= 5:
  print("You ara a little kid! ☺")
elif age <=12:
  print("You are a big kid! ☺")
elif age <= 19:
  print("You are a teenager ☺")
elif age >= 20:
  print("You are an adult already! ☻")
else:
  print("looks like you have not entere a number. Please, re-run the program.")



# =============================
print("Done!")