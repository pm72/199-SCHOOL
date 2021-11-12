Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
round(5.56417)
6
round(5.46417)
5

round(5.46417, 2)
5.46

round(5.46817, 2)
5.47

round(5.46817784125, 5)
5.46818


floor(5.89)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    floor(5.89)
NameError: name 'floor' is not defined. Did you mean: 'float'?

import math
floor(5.89)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    floor(5.89)
NameError: name 'floor' is not defined. Did you mean: 'float'?
math.floor(5.89)
5
math.floor(5.05)
5
math.floor(5)
5


math.floor(-5.56)
-6
math.floor(-5.00004)
-6


================================ RESTART: Shell ================================
import math as m
m.floor(5.89)
5
math.floor()
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    math.floor()
NameError: name 'math' is not defined


m.floor(7.02)
7


m.ceil(8.54)
9
m.ceil(8.0000000001)
9
m.ceil(8.000000000)
8
m.ceil(8)
8



================================ RESTART: Shell ================================
from math import *

floor(9.8)
9

cos(5.97)
0.951357034793342

================================ RESTART: Shell ================================
from math import floor, ceil
ceil(8.9)
9
floor(1.25)
1

floor(1.25, 2)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    floor(1.25, 2)
TypeError: math.floor() takes exactly one argument (2 given)

from math import pow, sqrt
pow(2, 5)
32.0

pow(5, 3.6987)
384.84013208747956
pow(-8, 3)
-512.0

8 ** 2
64

sqrt(64)
8.0

sqrt(81)
9.0

sqrt(-81)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    sqrt(-81)
ValueError: math domain error

sqrt(2)
1.4142135623730951
sqrt(3)
1.7320508075688772
sqrt(10)
3.1622776601683795
sqrt(9.547)
3.0898220013457087


factorial(5)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    factorial(5)
NameError: name 'factorial' is not defined


import math as m
m.factorial(5)
120
m.factorial(15)
1307674368000
m.factorial(153)
200634390509568239477828874698911718566246149616161171934231099284840946025238092339613294062603588435530393145048663047173051913507711632216305667129554900620296603188543122491838966881134795135997316305640071571629943041039657861120000000000000000000000000000000000000


x = 5, 89, 21, 51, -5.69, 10.02, -4.01, 11.58
min(x)
-5.69
max(x)
89


abs(-98)
98
abs(-9.8)
9.8


m.fabs(15)
15.0


import random as r
r.randrange(1, 10)
9
r.randrange(1, 10)
5
r.randrange(1, 10)
1
r.randrange(1, 10)
4

r.randint(1, 10)
7
r.randint(1, 10)
6
r.randint(1, 10)
1
r.randint(1, 10)
9
r.randint(1, 10)
2


r.random()
0.01277937959902764
r.random()
0.1663881038079772
r.random()
0.07061336032165699
r.random()
0.2907459095382291
r.random() * 10
0.23433059954833024
r.random() * 10
0.46267767701730134


r.random() * 10
4.6353307215698525
r.random() * 10
3.9906066550735284
r.random() * 10
7.528884576087332
r.random() * 10
0.06620688177579659

r.random() * 10
7.767705001647897
r.random() * 10
6.822613452085222

r.uniform(1, 10)
4.772456567840054
r.uniform(1, 10)
1.6499838291965445
r.uniform(1, 10)
9.485030063509537
r.uniform(1, 10)
6.072291687446031
r.uniform(1.18, 1.53)
1.5205387029010682
r.uniform(1.18, 1.53)
1.4820964727684764
r.uniform(1.18, 1.53)
1.3759322032199388
r.uniform(1.18, 1.53)
1.4278015787199843
r.uniform(1.18, 1.53)
1.3877806467476228


x = "Hello there!"
r.choice(x)
'l'
r.choice(x)
'e'
r.choice(x)
' '
r.choice(x)
' '
r.choice(x)
'e'


x = 5, 8, 9, 1, -9, 24, 11, -5, 2
r.choice(x)
11
r.choice(x)
1
r.choice(x)
8


x = 3, 5, 56, 1.05, 6.32, 'paata', 5, 'lol', 'gringo', True
r.choice(x)
True
r.choice(x)
5
r.choice(x)
3
r.choice(x)
1.05
r.choice(x)
56
r.choice(x)
'lol'
r.choice(x)
True
