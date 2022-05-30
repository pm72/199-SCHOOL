# bool  True / False

# a = True
# b = False
# print(f"a is {a} & b is {b}")
# print(f"a is {int(a)} & b is {int(b)}")
# print(f"a is {float(a)} & b is {float(b)}")
#
# print(bool(-15), bool(89), bool(1.89))
# print(bool(0), bool(0.0))
# print(bool('Paata'), bool(''), bool(' '))
#
# print(bool(None))

# შედარების ოპერაციები: < > <= >= == !=
a = 5
b = 12
# print(a < b)  # True
# print(a > b)  # False
# print(a <= b) # True
# print(a >= b) # False
# print(a == b) # False
# print(a != b) # True

# print(a + b >= a * b)
# print((a + b) >= (a * b))
# print(a + (b >= a) * b)
# print((a + b >= a) * b)
# print((a + b < a) * b)

# if, if .. else, if .. elif .. .. else
# age = int(input("Age: "))
# if age <= 5:
#   print("You are a little kid ☺☻")

# age = int(input("Age: "))
# if age <= 5:
#   print("You are a little kid ☺☻")
# else:
#   print("You are a big kid ☺☻♥")


age = int(input("Age: "))
if age <= 5:
  print("You are a little kid ☺☻")
elif age <=12:
  print("You are a big kid ☺☻♥")
elif age <= 19:
  print("You are a teenager ♥")
elif age >= 20:
  print("You are an adult already!")
else:
  print("Not a number. Please re-run the pogram and type a number")

print("\n\nDone!")