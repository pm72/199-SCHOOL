Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
int(5.78)
5

round(5.78)
6
round(5.48)
5
round(5.48478562, 2)
5.48
round(5.48578562, 2)
5.49
round(5.48578562, 4)
5.4858


import math as m
m.floor(5.89)
5
m.PI
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    m.PI
AttributeError: module 'math' has no attribute 'PI'. Did you mean: 'pi'?
m.pi
3.141592653589793

m.floor(8.002)
8

m.floor(-8.002)
-9

m.ceil(5.87)
6
m.ceil(5.0000001)
6

m.ceil(5)
5

m.ceil(-5.58)
-5
m.ceil(-5.98155)
-5


5 ** 2
25
2 ** 8
256

m.pow(5, 2)
25.0
m.pow(2, 8)
256.0
m.pow(2, 3.69)
12.90626814755402

m.sqrt(25)
5.0
m.sqrt(9)
3.0
m.sqrt(81)
9.0
m.sqrt(5)
2.23606797749979
m.sqrt(2)
1.4142135623730951
m.sqrt(3)
1.7320508075688772

m.sqrt(0)
0.0

m.pow(2, 0.5)
1.4142135623730951

m.pow(7, 7/8)
5.488589936824572


m.factorial(5)
120
m.factorial(15)
1307674368000
m.factorial(153)
200634390509568239477828874698911718566246149616161171934231099284840946025238092339613294062603588435530393145048663047173051913507711632216305667129554900620296603188543122491838966881134795135997316305640071571629943041039657861120000000000000000000000000000000000000


x = 5, 89, 21, 51, -5.69, 10.02, -4.01, 11.58
max(x)
89
min(x)
-5.69

abs(-9.84)
9.84
abs(14.84)
14.84


m.fabs(-9)
9.0


import random as r
r.randrange(1, 10)
4
r.randrange(1, 10)
7
r.randrange(1, 10)
8
r.randrange(1, 10)
4
r.randrange(1, 10)
7
r.randrange(1, 10)
5


r.randint(1, 10)
10
r.randint(1, 10)
8
r.randint(1, 10)
7
r.randint(1, 10)
6

r.randint(1, 10)
6
r.randint(1, 10)
5
r.randint(1, 10)
5
r.randint(1, 10)
2
r.randint(1, 10)
6


r.random()
0.39988162445810105
r.random()
0.0069686065849120515
r.random()
0.3155026801088924
r.random()
0.15615891085344247
r.random()
0.010155540786570105
r.random()
0.5083107959983624
r.random() * 10
8.75468429931291
r.random() * 10
5.322060219337162
r.random() * 10
0.7874437741888751
r.random() * 10
5.043176248130078


r.uniform(1, 10)
9.5737581573592
r.uniform(1, 10)
6.82767379195908
r.uniform(1, 10)
2.39289713103515
r.uniform(1, 10)
7.970169078444414

r.uniform(1.15, 1.51)
1.1550731021299319
r.uniform(1.15, 1.51)
1.444848118735973
r.uniform(1.15, 1.51)
1.3334292558138023
r.uniform(1.15, 1.51)
1.376882239489518
r.uniform(1.15, 1.51)
1.3031307740939968
r.uniform(1.15, 1.51)
1.1655940372429905



s = "Hello there!"
r.choice(s)
'H'
r.choice(s)
'r'
r.choice(s)
'h'
r.choice(s)
'r'
r.choice(s)
' '


s = 5, 8, 9, 1, -9, 24, 11, -5, 2
r.choice(s)
2
r.choice(s)
5
r.choice(s)
24
r.choice(s)
-5
r.choice(s)
-9

s = 11.25, -0.25, 1.02, 9.32, 8.01, -0.014, 1.6
s = 11.25, -0.25, 1.02, 9.32, 8.01, -0.014, 1.6
r.choice(s)
11.25
r.choice(s)
9.32
r.choice(s)
1.6
r.choice(s)
11.25


s = 3, 5, 56, 1.05, 6.32, 'paata', 5, 'lol', 'gringo', True
r.choice(s)
'lol'
r.choice(s)
True
r.choice(s)
56
r.choice(s)
'paata'
r.choice(s)
5
r.choice(s)
5
r.choice(s)
1.05
r.choice(s)
56
r.choice(s)
3
r.choice(s)
True


from random import *

coice(x)
Traceback (most recent call last):
  File "<pyshell#149>", line 1, in <module>
    coice(x)
NameError: name 'coice' is not defined. Did you mean: 'choice'?
choice(x)
21
choice(x)
-5.69
choice(x)
-5.69


asin(0.58)
Traceback (most recent call last):
  File "<pyshell#155>", line 1, in <module>
    asin(0.58)
NameError: name 'asin' is not defined. Did you mean: 'ascii'?
sin(58)
Traceback (most recent call last):
  File "<pyshell#156>", line 1, in <module>
    sin(58)
NameError: name 'sin' is not defined. Did you mean: 'bin'?

================================ RESTART: Shell ================================


from math import *
asin(0.58)
0.6187286906722511
asin(58)
Traceback (most recent call last):
  File "<pyshell#161>", line 1, in <module>
    asin(58)
ValueError: math domain error
asin(5.8)
Traceback (most recent call last):
  File "<pyshell#162>", line 1, in <module>
    asin(5.8)
ValueError: math domain error
asin(0.589)
0.6298208619278491


from math import ceil, floor
ceil(8.98)
9
floor(8.98)
8


sqrt(4)
2.0
