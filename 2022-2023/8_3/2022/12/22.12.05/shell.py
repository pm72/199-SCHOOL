Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import math as m
m.pi
3.141592653589793
m.sin(m.pi/2)
1.0
m.sin(m.pi/5)
0.5877852522924731


x1 = 39.55
x1 = m.radians(x1)
x1
0.6902777191637572

m.degress(x1)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    m.degress(x1)
AttributeError: module 'math' has no attribute 'degress'. Did you mean: 'degrees'?
>>> 
>>> m.degrees(x1)
39.55
>>> 
>>> 
>>> 
>>> 
>>> #  a = m.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
>>> 
>>> # p = (a + b + c) / 2
>>> # area = m.sqrt(p * (p - a) * (p - b) * (p - c))
>>> 
>>> 
>>> 
>>> x = 65
>>> chr(x)
'A'
>>> 
>>> 
>>> 97.5 - .29*97.5
69.225
>>> 
>>> 
>>> x = 1005
>>> # x = 5001
