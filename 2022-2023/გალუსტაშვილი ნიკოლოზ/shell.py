Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import math as m
m.pi
3.141592653589793
m.sin(m.pi / 5)
0.5877852522924731
0.5877852522924731
0.5877852522924731
r = 5.5

a = 2 * r * m.sin(m.pi / 5)
a
6.465637775217204

area = 3 * m.sqrt(3) / 2 * a ** 2
area
108.61120381651374

print(f"The area of the pentagon is {area}")
The area of the pentagon is 108.61120381651374

print(f"The area of the pentagon is {area:.2f}")
The area of the pentagon is 108.61

print(f"The area of the pentagon is {area:.2}")
The area of the pentagon is 1.1e+02
The area of the pentagon is 1.1e+02
SyntaxError: invalid syntax


r = eval(input("Enter the length from the center to a vertex: "))
Enter the length from the center to a vertex: 5.5
r
5.5
type(r)
<class 'float'>
r = eval(input("Enter the length from the center to a vertex: "))
Enter the length from the center to a vertex: 12
type(r)
<class 'int'>

================== RESTART: D:/199/გალუსტაშვილი ნიკოლოზ/3.1.py =================
Enter the length from the center to a vertex: 5.5
The area of the pentagon is 1.1e+02

================== RESTART: D:/199/გალუსტაშვილი ნიკოლოზ/3.1.py =================
Enter the length from the center to a vertex: 5.5
The area of the pentagon is 108.61




# 3.2
x1, y1 = eval(input("Enter point 1 (latitude and longitude) in degrees: "))
Enter point 1 (latitude and longitude) in degrees: 39.55, -116.25

# arccos()  ===>  m.acos()    arcsin()   m.asin() ...

x1 = m.radians(x1)
y1 = m.radians(y1)

x1, y1
(0.6902777191637572, -2.028945255443408)

m.sin(x1), m.sin(y1)
(0.636751347470152, -0.8968727415326884)


d = 10691.79183231593
print(f"The distance between the two points is {d:.2f} km")
The distance between the two points is 10691.79 km



# 3.3
# a = m.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
# b = ...  c = ...  d = ...  e = ...

# Heronis formula  =>>>>  area
# p1 = (a + b + e) / 2
# p2 = ...

# s1 = m.sqrt(p * (p - a) * (p - b) * (p - e))
# s2 = ...
# s = s1 + s2

# print(f"Area of rectangkle is {s:.2f}")


# 3.4
# tan()  =>>>> m.tan()



# 3.6
# chr()   ord()
chr(69)
'E'
chr(65)
'A'
chr(189)
'½'

chr(66)
'B'


ord('A')
65
>>> ord('B')
66
>>> ord('E')
69
>>> ord('½')
189
>>> 
>>> ord('a') - ord('A')
32
>>> ord('k') - ord('K')
32
>>> 
>>> 
>>> 
>>> #3.7
>>> from time import time
>>> time()
1670834947.577414
>>> 
>>> int(time())
1670834986
>>> int(time())
1670834990
>>> int(time())
1670834992
>>> 
>>> # [65..90]
>>> # gamosayenebelia naStiani gayofa  %
>>> 15 % 3
0
>>> 893 % 7
4
>>> 
>>> chr(int(time()) % 26 + 65)
'K'
>>> chr(int(time()) % 26 + 65)
'M'
>>> chr(int(time()) % 26 + 65)
'O'
