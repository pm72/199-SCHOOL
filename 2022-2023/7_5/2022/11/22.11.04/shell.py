Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
fabs(2.5)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    fabs(2.5)
NameError: name 'fabs' is not defined. Did you mean: 'abs'?
abs(25)
25


import math
math.pi
3.141592653589793

import math as m
m.pi
3.141592653589793

r = 13.57
m.pi * r ** 2
578.5082650360271
3.14 * r ** 2
578.2149860000001


m.ceil(2.1)
3
m.ceil(-2.1)
-2

m.floor(2.69)
2
m.floor(-2.69)
-3
m.floor(-2)
-2


round(3.56)
4

round(3.5)
4

round(2.5)
2

round(4.5)
4

round(14.5)
14
round(15.5)
16
round(16.5)
16
round(16.500000000001)
17


m.sqrt(16)
4.0
16 ** 0.5
4.0
>>> 
>>> 
>>> help(m.sqrt)
Help on built-in function sqrt in module math:

sqrt(x, /)
    Return the square root of x.

>>> 
>>> 
>>> 
>>> m.degrees(m.pi)
180.0
>>> m.degrees(m.pi / 2)
90.0
>>> m.degrees(3 * m.pi / 2)
270.0
>>> m.degrees(-0.3699)
-21.19370884188915
>>> 
>>> 
>>> m.radians(90)
1.5707963267948966
>>> m.radians(180)
3.141592653589793
>>> m.pi
3.141592653589793
