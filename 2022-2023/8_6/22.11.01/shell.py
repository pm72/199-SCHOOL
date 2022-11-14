Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> abs(15)
15
>>> abs(-115)
115
>>> +6
6
>>> -54
-54
>>> 
>>> 
>>> max(15, 25, 14, 58, 32, 27)
58
>>> min(15, 25, 14, 58, 32, 27)
14
>>> 
>>> sum(15, 25, 14, 58, 32, 27)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    sum(15, 25, 14, 58, 32, 27)
TypeError: sum expected at most 2 arguments, got 6
>>> 
>>> 
>>> help(sum)
Help on built-in function sum in module builtins:

sum(iterable, start=0, /)
    Return the sum of a 'start' value (default: 0) plus an iterable of numbers
    
    When the iterable is empty, return the start value.
    This function is intended specifically for use with numeric values and may
    reject non-numeric types.

>>> sum((15, 25, 14, 58, 32, 27))
171
>>> sum(start=15)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    sum(start=15)
TypeError: sum() takes no keyword arguments
>>> sum((), start=15)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    sum((), start=15)
TypeError: sum() takes no keyword arguments
>>> sum((1, 2), start=15)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    sum((1, 2), start=15)
TypeError: sum() takes no keyword arguments
>>> 
>>> 
>>> a = (15, 25, 14, 58, 32, 27)
>>> type(a)
<class 'tuple'>
>>> sum(a)
171
>>> len(a)
6
>>> 171 / 6
28.5
>>> sum(a) / len(a)
28.5
>>> average = sum(a) / len(a)
>>> average
28.5
>>> 
>>> 
>>> pow)_
SyntaxError: invalid syntax
>>> pow(2, 3)
8
>>> 2 ** 3
8
>>> 
>>> pow(2, 3, 2)
0
>>> 
>>> help(pow)
Help on built-in function pow in module builtins:

pow(x, y, z=None, /)
    Equivalent to x**y (with two arguments) or x**y % z (with three arguments)
    
    Some types, such as ints, are able to use a more efficient algorithm when
    invoked using the three argument form.

>>> pow(2, 3, 3)
2
>>> 
>>> 
>>> 
>>> 
>>> import math
>>> math.pi
3.141592653589793
>>> math.sqrt(16)
4.0
>>> 16 ** 0
1
>>> 16 ** 0.5
4.0
>>> -4 ** 2
-16
>>> (-4) ** 2
16
>>> -16 ** 0.5
-4.0
>>> 
>>> 
>>> import math as m
>>> m.pi
3.141592653589793
>>> 
