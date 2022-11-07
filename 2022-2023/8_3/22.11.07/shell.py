Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
abs(2)
2
abs(-2)
2

+1
1
-3
-3

max(15, 25, 21, 3, 69, 21, 58)
69
min(15, 25, 21, 3, 69, 21, 58)
3

sum(15, 25, 21, 3, 69, 21, 58)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    sum(15, 25, 21, 3, 69, 21, 58)
TypeError: sum() takes at most 2 arguments (7 given)

help(sum)
Help on built-in function sum in module builtins:

sum(iterable, /, start=0)
    Return the sum of a 'start' value (default: 0) plus an iterable of numbers
    
    When the iterable is empty, return the start value.
    This function is intended specifically for use with numeric values and may
    reject non-numeric types.



sum((15, 25, 21, 3, 69, 21, 58))
212

x = 15, 25, 21, 3, 69, 21, 58
x
(15, 25, 21, 3, 69, 21, 58)
type(x)
<class 'tuple'>

x[3]
3
x[0]
15
x[0] + x[3]
18
x[7]
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    x[7]
IndexError: tuple index out of range


sum(x)
212
len(x)
7
212/7
30.285714285714285

sum(x) / len(x)
30.285714285714285

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


pow(2, 3, 2)
0
pow(2, 3, 3)
2


import math as m
m.pi
3.141592653589793

r = 3
m.pi * r ** 2
28.274333882308138

m.fabs(2)
2.0
m.fabs(-8.9)
8.9
m.factorial(15)
1307674368000

!15
SyntaxError: invalid syntax

m.ceil(2.15)
3
m.ceil(-2.85)
-2

m.floor(7.89)
7
m.floor(-7.19)
-8

round(3.89)
4
round(3.19)
3

round(3.5)
4
round(2.5)
2


round(12.5)
12
round(9.5)
10
round(12.500000000000000000000001)
12
round(12.50000000000001)
13


m.sqrt(16)
4.0
>>> 16 ** 0.5
4.0
>>> 
>>> 
>>> m.degrees(m.pi)
180.0
>>> m.degrees(m.pi / 2)
90.0
>>> m.degrees(3 * m.pi / 2)
270.0
>>> m.degrees(m.pi / 6)
29.999999999999996
>>> m.degrees(m.pi / 3)
59.99999999999999
>>> m.degrees(m.pi / 4)
45.0
>>> 
>>> 
>>> m.radians(90)
1.5707963267948966
>>> m.radians(180)
3.141592653589793
>>> m.pi
3.141592653589793
>>> m.pi == m.radians(180)
True
>>> 
>>> 
