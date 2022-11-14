# s = pi * r ** 2    pi = 3.14159...
# l = 2 * pi * r

radius = eval(input("Enter the radius: "))
PI = 3.14159

area = round(PI * radius ** 2, 2)
length = round(2 * PI * radius, 2)

print("The area of the circle with radius", radius, "is", area)
print("The length of the circle with radius", radius, "is", length)



input()




# string    str  "paata"  'roma'  'c'  "5" "25874"  '1'
# numberic: int  float
# int: 15  29 -6 0 1 ...
# float:  2.89  -0.92  1.0 ...

# int('25') = 25  float('2.89') = 2.89
# int(1.56) = 1   int(3.98) = 3   float(5) = 5.0
# eval('4.56') = 4.56  eval(15) = 15
