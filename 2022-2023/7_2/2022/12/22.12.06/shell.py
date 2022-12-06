Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import math as m
m.pi
3.141592653589793
m.sin(m.pi / 5)
0.5877852522924731
m.sqrt(3)
1.7320508075688772



x1 = 39.55
x1 = m.radians(x1)
x1
0.6902777191637572
m.sin(x1)
0.636751347470152


# arcos()   =====> m.acos()   arcsin  ====>  m.asin()

d = 10691.79183231593
print(f"The distance is {d:.2f}")
The distance is 10691.79


print(f"The distance is {d:.2f} km")
The distance is 10691.79 km



# a = m.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

#  p1 = (a + b + e) / 2   p2 = (c + d + e) / 2

# S1 = m.sqrt(p1 * (p1 - a) * (p1 - b) * (p1 - e))

# s = s1 + s2



# tan()  ====> m.tan()



# chr()   ord()
chr(65)
'A'
chr(66)
'B'
chr(97)
'a'
chr(98)
'b'

ord('A')
65
ord('B|')
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    ord('B|')
TypeError: ord() expected a character, but string of length 2 found
ord('B')
66
>>> ord('a')
97
>>> 
>>> ord('a') - ord('A')
32
>>> ord('d') - ord('D')
32
>>> 
>>> 
>>> 
>>> from time import time
>>> time()
1670322027.0223083
>>> int(time())
1670322050
>>> int(time())
1670322052
>>> int(time())
1670322053
>>> 
>>> 
>>> 
>>> # print("Deductions:")
>>> # print("\tFederal Withholding (20.0%): $19.5")

>>> 
>>> 
>>> x = 1005
