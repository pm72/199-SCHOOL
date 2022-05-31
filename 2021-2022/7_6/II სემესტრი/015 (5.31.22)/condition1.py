#  bool   True/False
# a = True
# b = False
# print(f"a is {a} & b is {b}")
# print(f"a is {int(a)} & b is {int(b)}")
# print(f"a is {float(a)} & b is {float(b)}")

# print(bool(0), bool(0.0), bool(""), bool(None))
# print(bool(5), bool(0.025), bool(-17), bool(" "), bool("Paata"))


# პირობითი გამოსახულებები და ოპერატორები: < > <= >= == !=
a = 5
b = 12
# print(a < b)  # True
# print(a > b)  # Flase
# print(a <= b)  # True
# print(a >= b)  # Flase
# print(a == b)  # Flase
# print(a != b)  # True

# print(a + b >= a * b)   # 5 + 12 >= 5 * 12   ==> 17 >= 60   ==> False
# print((a + b) >= (a * b))   # 5 + 12 >= 5 * 12   ==> 17 >= 60   ==> False
# print(a + (b >= a) * b)   # 5 + True * 12   ==> 5 + 1 * 12 ===> 17
# print(a + (b >= a * b))   # 5 + (12 >= 60)  ==> 5 + Flase   ===> 5 + 0 ====> 5


# ლოგიკური კონსტრუქციები: if, if .. else, if .. elif .. .. else
# age = int(input("Age: "))
# if age <= 5:
#   print("You are a little kid ☺☻")

# age = int(input("Age: "))
# if age <= 5:
#   print("You are a little kid ☺☻")
# else:
#   print("You are a big kid ☺☻")

age = int(input("Age: "))
if age <= 5:
  print("You are a little kid ☺☻")
elif age <= 12:
  print("You are a big kid ☺☻")
elif age <= 19:
  print("You are a teenager ☺☻")
elif age >= 20:
  print("You are an adult already ♥")
else:
  print("Not a number. Please, re-run the program.")

print("\nDone!\n\n")