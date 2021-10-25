Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import math as m
m.floor(5.89)
5

int(5.89)
5

m.floor(5.005)
5

m.floor(-5.005)
-6

m.ceil(5.0259)
6
m.ceil(5.000000001)
6
m.ceil(-5.000000001)
-5
m.ceil(-5.9999899)
-5

m.ceil(5)
5
m.floor(9)
9


round(5.85471585)
6
round(5.45471585)
5

round(5.85471585, 2)
5.85
round(5.85871585, 2)
5.86
round(5.85871585, 4)
5.8587
round(5.85871585, 5)
5.85872


5 ** 2
25

2 ** 8
256

m.pow(5, 2)
25.0
m.pow(2, 8)
256.0


2 ** 3.69
12.90626814755402
m.pow(2, 3.69)
12.90626814755402


-2 ** 3
-8
pow(-2, 3)
-8
m.pow(-2, 3)
-8.0

pow(2, 3.5)
11.313708498984761

sqrt(4)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    sqrt(4)
NameError: name 'sqrt' is not defined

m.sqrt(4)
2.0
m.sqrt(25)
5.0
m.sqrt(81)
9.0

m = 90
m
90
m.ceil(5.98)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    m.ceil(5.98)
AttributeError: 'int' object has no attribute 'ceil'

import math as m
m.ceil(45.98)
46


m
<module 'math' (built-in)>
<module 'math' (built-in)>
SyntaxError: invalid syntax



m.sqrt(58 + 9*8 - 5 ** 2)
10.246950765959598

58 + 9*8 - 5 ** 2
105


m.factorial(5)
120
m.factorial(15)
1307674368000
m.factorial(153)
200634390509568239477828874698911718566246149616161171934231099284840946025238092339613294062603588435530393145048663047173051913507711632216305667129554900620296603188543122491838966881134795135997316305640071571629943041039657861120000000000000000000000000000000000000


x = 5, 89, 21, 51, -5.69, 10.02, -4.01, 11.58
type(x)
<class 'tuple'>

max(x)
89
min(x)
-5.69

sum(x) / len(x)
22.237500000000004

sum(1, 2, 3, 4) / len(1, 2, 3, 4)
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    sum(1, 2, 3, 4) / len(1, 2, 3, 4)
TypeError: sum() takes at most 2 arguments (4 given)

sum((1, 2, 3, 4)) / len((1, 2, 3, 4))
2.5


abs(-8.95)
8.95
abs(11.95)
11.95

m.fabs(-9.54)
9.54
m.fabs(11.00)
11.0


import random as r
r
<module 'random' from 'C:\\Python310\\lib\\random.py'>

r.randrange(1, 10)
3
r.randrange(1, 10)
3
r.randrange(1, 10)
9
r.randrange(1, 10)
2
r.randrange(1, 10)
2
r.randrange(1, 10)
4

r.randint(1, 10)
4
r.randint(1, 10)
10
r.randint(1, 10)
6
r.randint(1, 10)
8


r.random()
0.3642499170119001
r.random()
0.0019502356445312286
r.random()
0.2685551621325839
r.random()
0.18530135821662153
r.random()
0.6323887597033346
r.random() * 10
0.25941693771308283
r.random() * 10
8.540124955435163
r.random() * 10
0.13363426604306672
r.random() * 10
4.073744629360023
r.random() * 10
1.3793425965701878
r.random() * 10
7.341659978771978
r.random() * 10
1.9707503505481583


r.uniform(1, 10)
8.146608149548658
r.uniform(1, 10)
8.11482488789374
r.uniform(1, 10)
6.195219514108016
r.uniform(1, 10)
1.4394012767190034
r.uniform(1, 10)
5.3384803093045985
r.uniform(1, 10)
9.367521310569511


r.uniform(1.11, 1.15)
1.1237514014643237
r.uniform(1.11, 1.15)
1.1213034085252214
r.uniform(1.11, 1.15)
1.12141455482218
r.uniform(1.11, 1.15)
1.149811780087027
r.uniform(1.11, 1.15)
1.1339821826857666
r.uniform(1.11, 1.15)
1.1277483429787347



x = Hello there!
SyntaxError: invalid syntax. Perhaps you forgot a comma?


x = "Hello there!"
r.choice(x)
'H'
r.choice(x)
'l'
r.choice(x)
' '
r.choice(x)
'l'
r.choice(x)
'!'


x = 5, 8, 9, 1, -9, 24, 11, -5, 2
r.choice(x)
2
r.choice(x)
5
r.choice(x)
11


x = 11.25, -0.25, 1.02, 9.32, 8.01, -0.014, 1.6
r.choice(x)
1.6
r.choice(x)
11.25
r.choice(x)
8.01


x = 3, 5, 56, 1.05, 6.32, 'paata', 5, 'lol', 'gringo', True
r.choice(x)
3
r.choice(x)
1.05
r.choice(x)
'lol'
r.choice(x)
1.05
r.choice(x)
6.32
r.choice(x)
'paata'
r.choice(x)
'lol'
r.choice(x)
'paata'
r.choice(x)
1.05
