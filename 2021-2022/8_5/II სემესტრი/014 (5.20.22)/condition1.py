#   =====> ლოგიკური მნიშვნელობები  True / False <=====
# bool

# a = True
# b = False
# print(f"a is {a} & b is {b}")
# print(f"a is {int(a)} & b is {int(b)}")
# print(f"a is {float(a)} & b is {float(b)}")
# print(bool('True'), bool("False"), bool(""), bool(" "))
# print(bool(None))
#
# c = None
# print(id(c), type(c), c)
#
# d = str(True)
# print(id(d), type(d), d)


# =====> შედარების ოპერაციები <======
# < > <= >= == !=
# print(2 < 3)
# print(2 > 3)
# print(2 != 2)
# print(3*9 == 2+25)

# =====> ლოგიკური ოპერატორი if <======
# age = int(input("Age: "))
# if age <= 5:
#   print("You are a little kid! ☺☻")


# else
# age = int(input("Age: "))
# if age <= 5:
#   print("You are a little kid! ☺☻")
# else:
#   print("You ar a big kid! ☻☺")


# if .. elif .. elif .. .. else
try:
  age = int(input("Age: "))
  if age <= 5:
    print("You are a little kid! ☺☻")
  elif age <= 12:
    print("You ar a big kid! ☻☺")
  elif age <= 19:
    print("You ara a teenager! ☺☻")
  else:
    print("You ar an adult! ☺☻")
except ValueError:
  print("You not entered a integer number. Please, re-run the program.")