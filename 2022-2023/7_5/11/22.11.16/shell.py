Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
fabs
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    fabs
NameError: name 'fabs' is not defined. Did you mean: 'abs'?


import math as m
m.fabs(45)
45.0

help(m.acos)
Help on built-in function acos in module math:

acos(x, /)
    Return the arc cosine (measured in radians) of x.
    
    The result is between 0 and pi.


m.degrees(m.pi)
180.0
m.degrees(m.pi/2)
90.0

m.acos(1.57)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    m.acos(1.57)
ValueError: math domain error
m.acos(m.pi)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    m.acos(m.pi)
ValueError: math domain error


m.cos(1.57)
0.0007963267107332633


m.radians(90)
1.5707963267948966
1.5707963267948966
1.5707963267948966


m.acos(m.pi)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    m.acos(m.pi)
ValueError: math domain error

>>> 
>>> m.radians(15.26)
0.26633724385433466
>>> m.radians(90)
1.5707963267948966
>>> m.radians(74.74)
1.3044590829405618
>>> 
>>> m.radians(15.26) + m.radians(90) + m.radians(74.74)
3.141592653589793
>>> 
>>> 
>>> round(2.5)
2
>>> round(3.5)
4
>>> 
>>> 
>>> x = m.radians(47)
>>> x
0.8203047484373349
>>> y = m.degrees(m.pi / 7)
>>> y
25.714285714285715
