# s = pi * r ** 2   pi = 3.14159...
# l = 2 * pi * r
# round(value[, x])   round(2.5966912) = 3   round(2.56987, 2) = 2.57
# int('125') = 125
# float('1.247') = 1.247
# eval('25') = 25  eval(2.45) = 2.45


radius = eval(input("Enter the radius: "))
PI = 3.14159

area = PI * radius ** 2
length = 2 * PI * radius

print("The area of the citcle with radius", radius,
      "is", round(area, 2))
print("The length of the citcle with radius", radius,
      "is", round(length, 2))




# string    str    "paata"  'roma'  "c"  '5'  '1258445'  '1'
# numeric   int    float
# int   1 5 59 -5 0 45 ...
# float   1.58  -0.25  3.9   1.0
