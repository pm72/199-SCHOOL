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
# print(a + (b >= a) * b)   # 5 + True * 12   ==> 5 + 1 * 12 >= 17
# print(a + (b >= a * b))   # 5 + (12 >= 60)  ==> 5 + Flase   ===> 5 + 0 ====> 5