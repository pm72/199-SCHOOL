# s = pi * r ** 2    pi = 3.14159...
# l = 2 * pi * r

radius = eval(input("Enter the radius: "))
PI = 3.14159

area = round(PI * radius ** 2, 2)
length = round(2 * PI * radius, 2)

print("The area of the circle with radius", radius, "is", area)
print("The length of the circle with radius", radius, "is", length)



input()



# string   str  "paata"  'vova'  'c'  "5"  '18954'  '1'
# numeric  int  float
# int 10 58 -9 0 -11 1 ...
# float  2.52  1.08  -5.21  1.0 ...

# int('1') = 1   int(3.99999) = 3  int('1.58') = ERROR
# float('2.58') = 2.58  float('-5') = -5.0
# eval('25') = 25   eval('1.51') = 1.51
