Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
sum(12, 58, 21, 10, 42, 29)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    sum(12, 58, 21, 10, 42, 29)
TypeError: sum() takes at most 2 arguments (6 given)


help(sum)
Help on built-in function sum in module builtins:

sum(iterable, /, start=0)
    Return the sum of a 'start' value (default: 0) plus an iterable of numbers
    
    When the iterable is empty, return the start value.
    This function is intended specifically for use with numeric values and may
    reject non-numeric types.


sum((12, 58, 21, 10, 42, 29))
172

x = (12, 58, 21, 10, 42, 29)
x
(12, 58, 21, 10, 42, 29)

x[3]
10
x[2]
21
x[0]
12
x[0] + x[1]
70
x[7]
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    x[7]
IndexError: tuple index out of range

len(x)
6
172 / 6
28.666666666666668
sum(x) / len(x)
28.666666666666668

text = "Paata"
len(text)
5
text[0]
'P'
text[1]
'a'


text = "Paata Mamporia"
text[5]
' '
len(text)
14


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
pow(2, 3, 1)
0
pow(2, 3, 0)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    pow(2, 3, 0)
ValueError: pow() 3rd argument cannot be 0
pow(2, 3, -1)
0
pow(2, 3, -3)
-1
pow(2, 3, 2, 4)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    pow(2, 3, 2, 4)
TypeError: pow() takes at most 3 arguments (4 given)


pow(2, pow(3, 2))
512
2 ** 3 ** 2
512


import math
math.pi
3.141592653589793

r = 12.31
math.pi * r **2
476.06469851364824


import math as m
m.pi
3.141592653589793
m.pi * r ** 2
476.06469851364824


m.sqrt(25)
5.0
25 ** 0.5
5.0

help(m.sqrt)
Help on built-in function sqrt in module math:

sqrt(x, /)
    Return the square root of x.



m.pow(2, 6)
64.0
pow(2, 6)
64



round(2.56)
3
round(2.26)
2
>>> 
>>> round(3.5)
4
>>> round(2.5)
2
>>> round(4.5)
4
>>> round(14.5)
14
>>> 
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
>>> m.ceil(-0.89)
0
>>> 
>>> 
