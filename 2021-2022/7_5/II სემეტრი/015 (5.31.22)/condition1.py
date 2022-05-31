# bool  True/False
# a = True
# b = False
# print(f"a is {a} & b is {b}")
# print(f"a is {int(a)} & b is {int(b)}")
# print(f"a is {float(a)} & b is {float(b)}")

# print(bool(1), bool(-89), bool(0.56), bool(" "), bool("Paata"))
# print(bool(0), bool(0.0), bool(""), bool(None))


# შედარების ოპერაციები და ოპერატორები: < > <= >= == !=
# a = 5
# b = 12
# print(a < b)  # True
# print(a > b)  # False
# print(a <= b)  # True
# print(a >= b)  # False
# print(a == b)  # False
# print(a != b)  # True

# print(a + b <= a * b)  # 17 <= 60
# print((a + b) <= (a * b))  # 17 <= 60
# print(a + (b <= a) * b)  # 5 + False * 12   ==> 5 + 0 * 12   ==> 5
# print((a + b <= a) * b)  # 5 + False * 12   ==> (17 <= 5) * 12   ==> 0 * 12   ==> 0


# პირობითი კონსტრუქციები: if, if .. else, if .. elif .. .. else
age = int(input("Age: "))
if age <= 5:
  print("You are a little kid ☺☻")

print("\nDone!")