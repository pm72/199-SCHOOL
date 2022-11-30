Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
abs(25)
25
abs(-125)
125


+3
3
-8
-8


max(15, 28, 17, 20, 69, 24)
69
min(15, 28, 17, 20, 69, 24)
15

sum((15, 28, 17, 20, 69, 24))
173
len((15, 28, 17, 20, 69, 24))
6
173/6
28.833333333333332
sum((15, 28, 17, 20, 69, 24)) / len((15, 28, 17, 20, 69, 24))
28.833333333333332


type((15, 28, 17, 20, 69, 24))
<class 'tuple'>

x = (15, 28, 17, 20, 69, 24)
x
(15, 28, 17, 20, 69, 24)
x[2]
17
x[2] ** 2
289


var1 = x[2]
var1 + 18
35


pow(2, 3)
8
2 ** 3
8
>>> 
>>> pow(2, 3, 2)
0
>>> 
>>> 
>>> help(pow)
Help on built-in function pow in module builtins:

pow(base, exp, mod=None)
    Equivalent to base**exp with 2 arguments or base**exp % mod with 3 arguments
    
    Some types, such as ints, are able to use a more efficient algorithm when
    invoked using the three argument form.

>>> pow(2, 3, 2)
0
>>> pow(2, 3, 3)
2
>>> 
>>> 
>>> 2 ** 3 ** 2
512
>>> 2 ** 9
512
>>> pow(2, pow(3, 2))
512
