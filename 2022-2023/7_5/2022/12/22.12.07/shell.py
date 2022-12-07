Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import math as m
m.pi
3.141592653589793
a = 2 * r * m.sin(m.pi / 5)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    a = 2 * r * m.sin(m.pi / 5)
NameError: name 'r' is not defined

x = 15.8924571
print(f"{x:.2f}")
15.89



m.sqrt(m.pi)
1.7724538509055159




# arccos()  =====>   m.acos()    arcsin()  =====>  m.asin()

x = 39.55
x = m.radians(x)
x
0.6902777191637572
m.sin(x)
0.636751347470152

m.degrees(x)
39.55



#  a = m.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)   5-jer
#  p1 = (a + b + e) / 2
#  s1 = m.sqrt(p * (p - a) * (p - b) * (p - e))

#  p2 = ...
#  s2 = ...
# s = s1 + s2


>>> # tan()   ====> m.tan()
>>> 
>>> 
>>> 
>>> # chr()   ord()
>>> chr(69)
'E'
>>> chr(56)
'8'
>>> 
>>> 
>>> ord('E')
69
>>> 
>>> 
>>> from time import time
>>> time
<built-in function time>
>>> 
>>> time()
1670395864.2018483
>>> int(time())
1670395922
>>> int(time())
1670395924
>>> int(time())
1670395927
>>> 
