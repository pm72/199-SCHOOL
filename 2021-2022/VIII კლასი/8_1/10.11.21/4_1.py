num1 = 3
num2 = 5.78
num3 = 2 + 3j    # 'Class  <Complex>'


##print(num1, type(num1))
##print(num2, type(num2))
##print(num3, type(num3))



# -----------
##num1 = float(num1)
##print(num1, type(num1))
##
##num2 = int(num2)
##print(num2, type(num2))



# ---------
# real     imag
print(num3)
x1 = num3.real
x2 = num3.imag
print(x1, x2)

print()

print(str(num3), type(str(num3)))

print()

print(int(x1), int(x2))
print(int(num3.real), int(num3.imag))

print()

num4 = 7
num4 = complex(num4)
print(num4)

num4 = 17.85
num4 = complex(num4)
print(num4)
