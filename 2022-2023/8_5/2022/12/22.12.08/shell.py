Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import math as m
m.pi
3.141592653589793
m.sin(m.pi / 5)
0.5877852522924731


s = 108.6125896
print(round(s, 2))
108.61

print(f"{x}")
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print(f"{x}")
NameError: name 'x' is not defined
print(f"{s}")
108.6125896
print(f"{s:.2f}")
108.61


print(f"The area of the pentagon is s")
The area of the pentagon is s
print(f"The area of the pentagon is {s}")
The area of the pentagon is 108.6125896
print(f"The area of the pentagon is {s:.2}")
The area of the pentagon is 1.1e+02
print(f"The area of the pentagon is {s:.2f}")
The area of the pentagon is 108.61



x1, y1 = 39.55, -116.25
x1 = m.radians(x1)
y1 = m.radians(y1)

x1
0.6902777191637572
y1
-2.028945255443408
m.sin(x1)
0.636751347470152
m.cos(y1)
-0.44228869021900113

m.degrees(x1)
39.55
m.degrees(y1)
-116.25

# arccos()   ===> m.acos()   arcsin()  ===> m.asin() ....


d = 10691.79183231593
print(f"{The distance between the two points is {d:.2f} km}")
SyntaxError: invalid decimal literal
print(f"{The distance between the two points is {d:.2f} km")
SyntaxError: f-string: expecting '}'
print(f"The distance between the two points is {d:.2f} km")
The distance between the two points is 10691.79 km



# a = m.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)   5-jer
# b = ... c, d, e = ....

# p1 = (a + b + e) / 2
# p2 = ...

# s1 = m.sqrt(p * (p - a) * (p - b) * (p - e))
#
# s2 = ...

# s = s1 + s2



# tan()   ===> m.tan()


# chr()   ord()
chr(68)
'D'
chr(65)
'A'
chr(97)
'a'

ord('A')
65
ord('a')
97
ord('a') - ord('A')
32
ord('k') - ord('K')
32
>>> 
>>> 
>>> 
>>> 
>>> from time import time
>>> time()
1670481896.4282193
>>> int(time())
1670481925
>>> int(time())
1670481928
>>> int(time())
1670481929
>>> 
>>> 
>>> # [65..90]
>>> 
>>> 
>>> 
>>> #  print("Deductions:")
>>> #  print("\tFederal Withholding (20.0%): $19.5")
>>> 
>>> 
>>> 
>>> x = 1005
>>> # r = 5001
>>> # r = 5001
>>> 
