Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
pi
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    pi
NameError: name 'pi' is not defined
abs(-15)
15
abs(20)
20

+6
6
-9
-9

max(15, 21, 10, 5, 69, 22)
69
min(15, 21, 10, 5, 69, 22)
5

sum(15, 21, 10, 5, 69, 22)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    sum(15, 21, 10, 5, 69, 22)
TypeError: sum() takes at most 2 arguments (6 given)

help(sum)
Help on built-in function sum in module builtins:

sum(iterable, /, start=0)
    Return the sum of a 'start' value (default: 0) plus an iterable of numbers
    
    When the iterable is empty, return the start value.
    This function is intended specifically for use with numeric values and may
    reject non-numeric types.



sum((15, 21, 10, 5, 69, 22))
142

x = (15, 21, 10, 5, 69, 22)
z
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    z
NameError: name 'z' is not defined
x
(15, 21, 10, 5, 69, 22)
type(x)
<class 'tuple'>
x[3]
5

len(x)
6
142/6
23.666666666666668
sum(x) / len(x)
23.666666666666668


pow(2, 3)
8
2**3
8

pow(2, 3, 2)
0

help(pow)
Help on built-in function pow in module builtins:

pow(base, exp, mod=None)
    Equivalent to base**exp with 2 arguments or base**exp % mod with 3 arguments
    
    Some types, such as ints, are able to use a more efficient algorithm when
    invoked using the three argument form.

>>> 
>>> pow(2, 3, 3)
2
>>> 
>>> 
>>> import math as m
>>> m.pi
3.141592653589793
>>> 
>>> r = 12.68
>>> m.pi * r ** 2
505.11280666653556
>>> 
>>> 
>>> m.ceil(2.36)
3
>>> m.ceil(-2.36)
-2
>>> 
>>> m.floor(2.89)
2
>>> m.floor(-2.89)
-3
>>> 
>>> 
>>> max((15, 25, 63))
63
