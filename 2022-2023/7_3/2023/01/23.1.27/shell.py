Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

=================== RESTART: D:/199/7_3/2023/addition_quiz.py ==================
What is 2 + 4? 6
2 + 4 = 6 is True

========== RESTART: D:/199/7_3/2023/addition_quiz.py ==========
What is 3 + 7? 11
3 + 7 = 11 is False

========== RESTART: D:/199/7_3/2023/addition_quiz.py ==========
What is 9 + 0? 9
9 + 0 = 9 is True

========== RESTART: D:/199/7_3/2023/addition_quiz.py ==========
What is 8 + 1? 2
8 + 1 = 2 is False
8 + 1 is 9


import random as r

r.randrange(0, 1)
0
r.randrange(0, 1)
0
r.randrange(0, 1)
0
r.randrange(0, 1)
0
r.randint(0, 1)
1
r.randint(0, 1)
0

r.random()
0.6492124463396782
r.random()
0.4841428121399505
r.random()
0.26503846650647445

r.uniform(5, 5.1)
5.021154337429892
r.uniform(5, 5.1)
5.076668635838674


r.uniform(5, 5.0001)
5.000033227788382
r.uniform(5, 5.0001)
5.000013779121981
r.uniform(5, 5.0001)
5.000004278365309



x = range(1, 61)
x
range(1, 61)
*x
SyntaxError: can't use starred expression here
print(*x)
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60


r.choice(x)
45
r.choice(x)
59
r.choice(x)
32



========== RESTART: D:/199/7_3/2023/simple_if_demo.py =========
Enter an integer: 64
Hi even!

========== RESTART: D:/199/7_3/2023/simple_if_demo.py =========
Enter an integer: 20
Hi five!
Hi even!

========== RESTART: D:/199/7_3/2023/simple_if_demo.py =========
Enter an integer: 19

========== RESTART: D:/199/7_3/2023/simple_if_demo.py =========
Enter an integer: 19
Hi odd

========== RESTART: D:/199/7_3/2023/simple_if_demo.py =========
Enter an integer: 15
Hi five!
Hi odd

========== RESTART: D:/199/7_3/2023/simple_if_demo.py =========
Enter an integer: 4
Hi even!
Hi even!


not 5
False

not 0
True

not True
False

not False
True


a = None
a += 1
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    a += 1
TypeError: unsupported operand type(s) for +=: 'NoneType' and 'int'


a = 56
a
56


>>> a = None
>>> bool(a)
False
>>> 
>>> not a
True
>>> 
>>> 
>>> x = r.randint(0, 9)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    x = r.randint(0, 9)
NameError: name 'r' is not defined
>>> 
>>> 
>>> import random as r
>>> x = r.randint(0, 9)
>>> y = r.randint(0, r)
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    y = r.randint(0, r)
  File "C:\Program Files\Python310\lib\random.py", line 370, in randint
    return self.randrange(a, b+1)
TypeError: unsupported operand type(s) for +: 'module' and 'int'
y = r.randint(0, x)

x, y
(9, 8)
x, y
(9, 8)
x, y
(9, 8)
x, y
(9, 8)
