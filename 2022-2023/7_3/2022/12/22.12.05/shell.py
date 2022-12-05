Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import math as m
>>> from math import sqrt, sin, pi
>>> sin(pi / 5)
0.5877852522924731
>>> ##area = 3 * (sqrt(3) / 3) * a ** 2

>>> x1 = 39.55
>>> x1 = m.radians(x1)
>>> x1
0.6902777191637572
>>> 
>>> m.degrees(x1)
39.55
>>> 
>>> # arccos()  ===> acos()
>>> # arcsin()  ===> asin()
>>> 
>>> 
>>> # a = m.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)   5-jer
>>> 

>>> # p = (a + b + c) / 2   2-jer
>>> 
>>> # area1 = m.sqrt(p * (p - a) * (p - b) * (p - c))   2-jer
>>> 
>>> 
x = 65
chr(x)
'A'

x =115
chr(x)
's'

x = 200
chr(x)
'È'

x = 0
chr(x)
'\x00'

x = 48
chr(x)
'0'

ord('D')
68
ord('0')
48


from time import time
time()
1670235234.7999337

int(time)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    int(time)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'builtin_function_or_method'
int(time())
1670235267
1670235267
1670235267

int(time()) % 128
94
chr(int(time()) % 128)
'\x00'
chr(int(time()) % 128)
'\x07'
chr(int(time()) % 128)
'\x18'
chr(int(time()) % 128)
'\x1d'
chr(int(time()) % 128)
'('
chr(65+26)
'['
chr(65+25)
'Z'
chr(97+25)
'z'

'a'.upper()
'A'



x = 1156
x = 158698



97.5 - 0.2 * 97.5
78.0
97.5 - .29*97.5
69.225


100 - 0.22 * 100
78.0


# x = 1005
# y = 5001


print("Deductions:\nFederal Withholding (20.0%): $19.5:")
Deductions:
Federal Withholding (20.0%): $19.5:

print("Deductions:\n\tFederal Withholding (20.0%): $19.5:")
Deductions:
	Federal Withholding (20.0%): $19.5:
