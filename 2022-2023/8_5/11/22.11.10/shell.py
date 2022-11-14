Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
abs(17)
17
abs(-17)
17

+6
6
-5
-5


max(12, 85, 21, 4, 78, 33, 52)
85
min(12, 85, 21, 4, 78, 33, 52)
4
sum(12, 85, 21, 4, 78, 33, 52)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    sum(12, 85, 21, 4, 78, 33, 52)
TypeError: sum() takes at most 2 arguments (7 given)


help(sum)
Help on built-in function sum in module builtins:

sum(iterable, /, start=0)
    Return the sum of a 'start' value (default: 0) plus an iterable of numbers
    
    When the iterable is empty, return the start value.
    This function is intended specifically for use with numeric values and may
    reject non-numeric types.



x = 12, 85, 21, 4, 78, 33, 52
x
(12, 85, 21, 4, 78, 33, 52)
type(x)
<class 'tuple'>
x[1]
85
x[6]
52
x[7]
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    x[7]
IndexError: tuple index out of range

sum((12, 85, 21, 4, 78, 33, 52))
285

sum(x)
285
sum(x[1], x[2])
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    sum(x[1], x[2])
TypeError: 'int' object is not iterable
x
(12, 85, 21, 4, 78, 33, 52)
x[1]
85
sum((x[1], x[2]))
106


sum(10, 12)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    sum(10, 12)
TypeError: 'int' object is not iterable


sum((x[1], x[2]), start=2)
108
sum((x[1], x[2]), start=12)
118


sum((x[1], x[2]))
106


sum(x)
285
type(x)
<class 'tuple'>
x
(12, 85, 21, 4, 78, 33, 52)
len(x)
7
285/7
40.714285714285715
sum(x) / len(x)
40.714285714285715
x = (0) + x
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    x = (0) + x
TypeError: unsupported operand type(s) for +: 'int' and 'tuple'

x = ([0] + list(x))
x
[0, 12, 85, 21, 4, 78, 33, 52]
x = tuple(x)
x
(0, 12, 85, 21, 4, 78, 33, 52)


sum(x) / len(x)
35.625

[0] + [1, 2, 3]
[0, 1, 2, 3]


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
pow(2, 3, 4, 4)
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    pow(2, 3, 4, 4)
TypeError: pow() takes at most 3 arguments (4 given)



round(3.56)
4
round(3.5)
4
round(2.5)
2
round(3.5)
4
round(4.5)
4
round(14.5)
14
round(14.5000000001)
15
round(14.500000000000000000000000000001)
14


round(2/3, 2)
0.67
round(0.5)
0
round(0.5, 2)
0.5
round(0.5, 1)
0.5
round(0.5, 0)
0.0
round(5, 0)
5



import math
math.pi
3.141592653589793

r = 3

m.pi * r ** 2
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    m.pi * r ** 2
NameError: name 'm' is not defined

math.pi * r ** 2
28.274333882308138


import math as m
>>> m.pi
3.141592653589793
>>> 
>>> 
>>> m.fabs(5)
5.0
>>> abs(5)
5
>>> abs(2.58)
2.58
>>> m.fabs(5.25)
5.25
>>> m.fabs(-5.25)
5.25
>>> 5.25
5.25
>>> 
>>> 
>>> 
>>> m.ceil(2.16)
3
>>> m.ceil(-2.96)
-2
>>> 
>>> m.floor(2.56)
2
>>> m.floor(-2.56)
-3
