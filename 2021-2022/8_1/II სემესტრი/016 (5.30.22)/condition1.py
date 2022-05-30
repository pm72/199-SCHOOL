# bool   True/False
# a = True
# b = False
# print(f"a is {a} & b is {b}")
# print(f"a is {int(a)} & b is {int(b)}")
# print(f"a is {float(a)} & b is {float(b)}")

# print(bool(0), bool(0.0), bool(""), bool(None))
# print(bool(15), bool(-5), bool(0.89), bool(" "), bool("Paata"))

# პირობითი ოპერატორები: < > <= >= == !=
# a = 5
# b = 12
# print(a < b)  # True
# print(a > b)  # False
# print(a <= b)  # True
# print(a >= b)  # False
# print(a == b)  # False
# print(a != b)  # True

# print(a + b >= a * b)
# print((a + b) >= (a * b))
# print(a + (b >= a) * b)   # 5 + true * 12   ===> 5 + 1 * 12   ===>  17
# print(a + (b == a) * b)   # 5 + False * 12   ===> 5 + 0 * 12   ===>  5
# print((a + b == a) * b)   # 12 + False * 12   ===> 0 * 12   ===>  0


# if, if .. else, if .. elif .. .. else
# age = int(input("Age: "))
# if age <= 5:
#   print("You are a little kid ☺☻")

age = int(input("Age: "))
if age <= 5:
  print("You are a little kid! ☺☻")
elif age <= 12:
  print("You are a big kid! ☺☻")
elif age <= 19:
  print("You are a teenager! ☺☻")
elif age >= 20:
  print("You are an adult already! ♥")
else:
  print("Not a integer number. Please, re-run the program.")


print("\nDone!")