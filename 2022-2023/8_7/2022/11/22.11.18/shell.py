Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
help(eval)
Help on built-in function eval in module builtins:

eval(source, globals=None, locals=None, /)
    Evaluate the given source in the context of globals and locals.
    
    The source may be a string representing a Python expression
    or a code object as returned by compile().
    The globals must be a dictionary and locals can be any mapping,
    defaulting to the current globals and locals.
    If only globals is given, locals defaults to it.



import math as m
help(m.acos)
Help on built-in function acos in module math:

acos(x, /)
    Return the arc cosine (measured in radians) of x.
    
    The result is between 0 and pi.



m.ceil(2.189555)
3

m.ceil(-10.58)
-10

m.floor(5.98)
5
m.floor(-5.18)
-6


m.sqrt(16)
4.0
16 ** 0
1
16 ** 0.5
4.0
m.sqrt(-16)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    m.sqrt(-16)
ValueError: math domain error
-16 ** 0.5
-4.0

(-16)**0.5
(2.4492935982947064e-16+4j)
2 **0.5
1.4142135623730951


m.degrees(m.pi)
180.0
m.radians(90)
1.5707963267948966
m.radians(180)
3.141592653589793



help(m.acos)
Help on built-in function acos in module math:

acos(x, /)
    Return the arc cosine (measured in radians) of x.
    
    The result is between 0 and pi.

>>> 
>>> 
>>> 
============ RESTART: D:/199/8_7/22.11.18/Compute angles.py ============
Enter three points: 1, 1, 6.5, 1, 6.5, 2.5
The angles are: 0.27 1.57 1.3
>>> 
>>> 0.27 + 1.57 + 1.3
3.14
>>> 
============ RESTART: D:/199/8_7/22.11.18/Compute angles.py ============
Enter three points: 1, 1, 6.5, 1, 6.5, 2.5
The angles are: 0.27 1.57 1.3
>>> 
============ RESTART: D:/199/8_7/22.11.18/Compute angles.py ============
Enter three points: m.degrees
Traceback (most recent call last):
  File "D:/199/8_7/22.11.18/Compute angles.py", line 3, in <module>
    x1, y1, x2, y2, x3, y3 = eval(input("Enter three points: "))
TypeError: cannot unpack non-iterable builtin_function_or_method object
>>> 
============ RESTART: D:/199/8_7/22.11.18/Compute angles.py ============
Enter three points: 1, 1, 6.5, 1, 6.5, 2.5
The angles are: 15.26 90.0 74.74
