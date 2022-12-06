Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import math as m
m.pi
3.141592653589793
m.sin(m.pi / 5)
0.5877852522924731


m.sqrt(16)
4.0



x1 = 39.55
x1 = m.radians(x1)
x1
0.6902777191637572

m.degrees(x1)
39.55

x1 = 100
x1 = m.radians(x1)
x1
1.7453292519943295


print(f"Distance is {10691.79183231593:.2f}")
Distance is 10691.79
print(f"Distance is {10691.79183231593:.f}")
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    print(f"Distance is {10691.79183231593:.f}")
ValueError: Format specifier missing precision
print(f"Distance is {10691.79183231593:.0f}")
Distance is 10692



# a = m.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)   5-jer

# p = (a + b + c) / 2
# area1 = m.sqrt(p * (p - a) * (p - b) * (p - c))

# area = area1 + area2



# chr()   ord()
chr(65)
'A'
chr(66)
'B'
chr(97)
'a'

ord('A')
65
ord('B')
66
>>> ord('a')
97
>>> 
>>> ord('a') - ord('A')
32
>>> 
>>> ord('s') - ord('S')
32
>>> 
>>> 
>>> from time import time
>>> time()
1670319091.081209
>>> int(time())
1670319119
>>> int(time())
1670319121
>>> 
>>> chr(64)
'@'
>>> 
>>> 
>>> 
>>> #  print("Deductions:")
>>> #  print("\tFederal Withholding (20.0%): $19.5")
>>> 
>>> 
>>> x = 1005
