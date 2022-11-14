Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import math as m
>>> 
>>> m.pi
3.141592653589793
>>> math.pi
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    math.pi
NameError: name 'math' is not defined
>>> 
>>> 
>>> m.fabs(-25.89)
25.89
>>> m.fabs(5)
5.0
>>> 
>>> 
>>> m.ceil(2.32)
3
>>> m.ceil(-2.32)
-2
>>> m.floor(5.89)
5
>>> m.floor(-5.89)
-6
>>> m.floor(-5.09)
-6
>>> 
>>> 
>>> m.sqrt(16)
4.0
>>> 16 ** 0.5
4.0
>>> 
>>> help(m.sqrt)
Help on built-in function sqrt in module math:

sqrt(...)
    sqrt(x)
    
    Return the square root of x.

>>> 
============= RESTART: D:/199/7_3/22.10.31/3_1 compute angles.py =============
Enter three points: 1, 1, 6.5, 1, 6.5, 2.5
The three angles are 0.27 1.57 1.3
>>> 
============= RESTART: D:/199/7_3/22.10.31/3_1 compute angles.py =============
Enter three points: 1, 1, 6.5, 1, 6.5, 2.5
The three angles are 15.26 90.0 74.74
>>> 
