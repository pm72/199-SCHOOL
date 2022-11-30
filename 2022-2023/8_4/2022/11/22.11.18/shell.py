Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
max(15, 25, 21, 69, 32, 14, 8)
69


help(max)
Help on built-in function max in module builtins:

max(...)
    max(iterable, *[, default=obj, key=func]) -> value
    max(arg1, arg2, *args, *[, key=func]) -> value
    
    With a single iterable argument, return its biggest item. The
    default keyword-only argument specifies an object to return if
    the provided iterable is empty.
    With two or more arguments, return the largest argument.


min(15, 25, 21, 69, 32, 14, 8)
8

sum(15, 25, 21, 69, 32, 14, 8)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    sum(15, 25, 21, 69, 32, 14, 8)
TypeError: sum() takes at most 2 arguments (7 given)


help(sum)
Help on built-in function sum in module builtins:

sum(iterable, /, start=0)
    Return the sum of a 'start' value (default: 0) plus an iterable of numbers
    
    When the iterable is empty, return the start value.
    This function is intended specifically for use with numeric values and may
    reject non-numeric types.



sum((15, 25, 21, 69, 32, 14, 8))
184

x = (15, 25, 21, 69, 32, 14, 8)
x
(15, 25, 21, 69, 32, 14, 8)

x[0]
15
x[5]
14
x[7]
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    x[7]
IndexError: tuple index out of range


sum(x)
184
len(x)
7
184/7
26.285714285714285
sum(x) / len(7)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    sum(x) / len(7)
TypeError: object of type 'int' has no len()
sum(x) / len(x)
26.285714285714285


pow(2, 3)
8
2 ** 3
8
pow(2, 3, 2)
0
help(pow)
Help on built-in function pow in module builtins:

pow(base, exp, mod=None)
    Equivalent to base**exp with 2 arguments or base**exp % mod with 3 arguments
    
    Some types, such as ints, are able to use a more efficient algorithm when
    invoked using the three argument form.

pow(2, 3, 3)
2
pow(2, 3, 4)
0


pow(2, 3, 4, 5)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    pow(2, 3, 4, 5)
TypeError: pow() takes at most 3 arguments (4 given)
pow(2, 3, 0)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    pow(2, 3, 0)
ValueError: pow() 3rd argument cannot be 0


import math as m
m.pi
3.141592653589793

m.sqrt(16)
4.0
16 ** 0.5
4.0
>>> 
>>> 
>>> m.fabs(-9)
9.0
>>> abs(-9)
9
>>> abs(-9.9)
9.9
>>> 
>>> m.ceil(2.12)
3
>>> m.ceil(-2.12)
-2
>>> 
>>> m.floor(3.89)
3
>>> m.floor(-3.19)
-4
>>> 
>>> 
>>> m.degrees(m.pi)
180.0
>>> 
>>> m.degrees(m.pi/2)
90.0
>>> m.degrees(m.pi/3)
59.99999999999999
