# ლოგიკური მნიშნელობები: True / False
# bool

# a = True
# b = False
# print(f"a is {a} % b is {b}")
# print(f"a is {int(a)} % b is {int(b)}")

# print(bool(1), bool(0))
# print(bool(-89), bool(1.96))
# print(bool('True'), bool('False'), bool(''), bool(' '))
# print(bool(None))
#
# a = None
# print(id(a), type(a), a)
#
# a = 4.58
# print(id(a), type(a), a)


# ლოგიკური გამოსახულებები
# ლოგიკური ოპერატორები: < > <= >= == !=
# print(2 < 3)
# print(5 > 8)
# print(4 != 4)
# print(17 == 17)
# print(3*9 == 3*3+18)


# ლოგიკური ოპერატორი  if,  if .. else,  if .. elif .. elif .. .. else
# age = int(input("Age: "))
# if age <= 5:
#   print("You are a little kid! ☺☻")

# else
# age = int(input("Age: "))
# if age <= 5:
#   print("You are a little kid! ☺☻")
# else:
#   print("You ar a big kid! ☺☻")


# elif
age = 0
try:
  while age <= 0:
    age = int(input("Age: "))

  if age <= 5:
    print("You are a little kid! ☺☻")
  elif age <= 12:
    print("You ar a big kid! ☺☻")
  elif age <= 19:
    print("You ar a teenager! ☺☻")
  else:
    print("You ar an adult already! ☺☻")
except ValueError:
  print("Sorry, you entered not an integer number. Please re-run the program!")


# =================
print("Done!")