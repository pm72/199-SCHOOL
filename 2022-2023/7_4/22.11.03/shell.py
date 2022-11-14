Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
help(max)
Help on built-in function max in module builtins:

max(...)
    max(iterable, *[, default=obj, key=func]) -> value
    max(arg1, arg2, *args, *[, key=func]) -> value
    
    With a single iterable argument, return its biggest item. The
    default keyword-only argument specifies an object to return if
    the provided iterable is empty.
    With two or more arguments, return the largest argument.

fabs(-56)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    fabs(-56)
NameError: name 'fabs' is not defined. Did you mean: 'abs'?


import math
math.fabs(-56)
56.0

help(math.fabs)
Help on built-in function fabs in module math:

fabs(x, /)
    Return the absolute value of the float x.

abs(-56)
56
abs(-5.6)
5.6


help(help)
Help on _Helper in module _sitebuiltins object:

class _Helper(builtins.object)
 |  Define the builtin 'help'.
 |  
 |  This is a wrapper around pydoc.help that provides a helpful message
 |  when 'help' is typed at the Python interactive prompt.
 |  
 |  Calling help() at the Python prompt starts an interactive help session.
 |  Calling help(thing) prints help for the python object 'thing'.
 |  
 |  Methods defined here:
 |  
 |  __call__(self, *args, **kwds)
 |      Call self as a function.
 |  
 |  __repr__(self)
 |      Return repr(self).
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)




import math as m

m.pi
3.141592653589793
m.pow(m.pi, 3)
31.006276680299816

r = 12.69
m.pi * r ** 2
505.90982872275123


m.sqrt(16)
4.0
4 ** 0.5
2.0
16 ** 0.5
4.0


m.ceil(2.3)
3

m.ceil(-2.3)
-2

m.floor(3.9)
3
m.floor(-3.9)
-4

round(1.5)
2
round(2.5)
2
round(3.5)
4
round(4.5)
4
round(4.50000000001)
5
round(4.5000000000)
4

m.degrees(1.57)
89.95437383553924
m.degrees(m.pi)
180.0
m.degrees(2 * m.pi / 3)
119.99999999999999
m.degrees(2 * (m.pi / 3))
119.99999999999999

========== RESTART: D:/199/7_4/22.11.03/3_1 Compute angels.py ==========
Enter three points: 1, 1, 6.5, 1, 6.5, 2.5
Traceback (most recent call last):
  File "D:/199/7_4/22.11.03/3_1 Compute angels.py", line 9, in <module>
    A = acos((a * a - b * b - c * c) / (-2 * b * c))
NameError: name 'acos' is not defined
>>> 
========== RESTART: D:/199/7_4/22.11.03/3_1 Compute angels.py ==========
Enter three points: 1, 1, 6.5, 1, 6.5, 2.5
The three angles are  0.27 1.57 1.3
>>> \
... 
... 
... 
... 
... 
...   asa
...   
SyntaxError: unexpected indent
>>> 
>>> help(m.acos)
Help on built-in function acos in module math:

acos(x, /)
    Return the arc cosine (measured in radians) of x.
    
    The result is between 0 and pi.

>>> 
========== RESTART: D:/199/7_4/22.11.03/3_1 Compute angels.py ==========
Enter three points: 1, 1, 6.5, 1, 6.5, 2.5
The three angles are  15.26 90.0 74.74
