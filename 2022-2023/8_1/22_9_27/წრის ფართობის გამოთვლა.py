# s = pi * r ** 2
# pi = 3.14159...

radius = eval(input("Enter the radius: "))
PI = 3.14159

area = round(PI * radius ** 2, 2)
length = round(2 * PI * radius, 2)

print("The area of the circle with radius", radius, "is", area)
print("The length of the circle with radius", radius, "is", length)


input()



# string    str   "paata"  'roma'   'x'  "5"  '15874'  '1.58' '1'
# numeric   int  float
# int: 15 29 -62 0 1 ...  float: 1.558  -0.241 1.0 ...

# int('12') = 12  int(2.3) = 2  int(1.98) = 1
# float(2.41) = 2.41  float('5') = 5.0  float(7) = 7.0
# eval('24') = 24   eval('1.89') = 1.89
