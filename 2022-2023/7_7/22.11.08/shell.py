Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
abs(58)
58
abs(-58)
58

+6
6
-3
-3

max(15, 24, 11, 53, 8, 21, 44)
53
min(15, 24, 11, 53, 8, 21, 44)
8

sum(15, 24, 11, 53, 8, 21, 44)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    sum(15, 24, 11, 53, 8, 21, 44)
TypeError: sum() takes at most 2 arguments (7 given)

help(sum)
Help on built-in function sum in module builtins:

sum(iterable, /, start=0)
    Return the sum of a 'start' value (default: 0) plus an iterable of numbers
    
    When the iterable is empty, return the start value.
    This function is intended specifically for use with numeric values and may
    reject non-numeric types.


sum((15, 24, 11, 53, 8, 21, 44))
176


x = 15, 24, 11, 53, 8, 21, 44
x
(15, 24, 11, 53, 8, 21, 44)
type(x)
<class 'tuple'>

x[0]
15
x[7]
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    x[7]
IndexError: tuple index out of range

len(x)
7
176/7
25.142857142857142
sum(x) / len(x)
25.142857142857142


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


import math
math.pi
3.141592653589793
math.sqrt(16)
4.0
16 ** 0.5
4.0
math.sqrt(17)
4.123105625617661
_ **2
17.0


import math as m
m.pi
3.141592653589793

m.ceil(2.1)
3
m.ceil(-2.1)
-2

m.floor(2.9)
2
m.floor(-2.9)
-3


round(3.56)
4

round(2.5)
2


round(3.5)
4
round(2.500000000001)
3



-12 % 5
3
>>> 
>>> 
>>> 
>>> m.pi
3.141592653589793
>>> 
>>> m.degrees(m.pi)
180.0
>>> m.degrees(m.pi / 2)
90.0
>>> m.degrees(m.pi / 4)
45.0
>>> m.degrees(m.pi / 3)
59.99999999999999
>>> m.degrees(m.pi / 6)
29.999999999999996
>>> 
>>> 
>>> m.rad
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    m.rad
AttributeError: module 'math' has no attribute 'rad'
>>> m.radians(90)
1.5707963267948966
>>> m.radians(180)
3.141592653589793
