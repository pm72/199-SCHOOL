x, y, z = eval(input("Enter three numbers: "))  # 2, 3, 6

print("(x < y and y < z) is", x < y and y < z)  # True
print("(x < y or y < z) is", x < y or y < z)    # True
print("not (x < y) is", not (x < y))            # False
print("(x < y < z) is", x < y < z)              # True
print("not(x < y < z) is", not (x < y < z))     # False
