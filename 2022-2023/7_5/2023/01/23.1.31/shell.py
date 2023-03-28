Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

=================== RESTART: D:/199/7_5/2023/addition_quiz.py ==================
What is 9 + 1? 10

= RESTART: D:/199/7_5/2023/addition_quiz.py
What is 8 + 5? 13
8 + 5 = 13 is True

= RESTART: D:/199/7_5/2023/addition_quiz.py
What is 8 + 8? 15
8 + 8 = 15 is False

= RESTART: D:/199/7_5/2023/addition_quiz.py
What is 4 + 8? 11
4 + 8 = 11 is False
4 + 8 = 12


r.randrange(0, 5)
3
r.randrange(0, 5)
1
r.randrange(0, 5)
4
r.randrange(0, 5)
2
r.randrange(0, 5)
4

r.randrange(0, 1)
0
r.randrange(0, 1)
0
r.randrange(0, 1)
0
r.randint(0, 1)
0

r.randint(0, 1)
1
r.randint(0, 1)
0
r.randint(0, 1)
1
r.randint(0, 1)
1


r.random()
0.6039074765083963
r.random()
0.5832382870364299


for i in range(20):
    print(r.random())

    
0.5729057696455229
0.36365256909435517
0.250518871490198
0.5771166391567806
0.46270710746812294
0.5219263432708214
0.864312692758504
0.06668081309569007
0.823443294515097
0.9951841607722994
0.07224827601979211
0.5279153274706528
0.9790314379831676
0.3258992746082686
0.22376009541724962
0.24626342330764095
0.20759769421253405
0.9814124371848272
0.9489676476960097
0.7491053968210548


r.uniform(5.5, 5.55)
5.519072837358713
r.uniform(5.5, 5.55)
5.535290514317838

for i in range(20):
    print(r.uniform(5.5, 5.55))

    
5.538707159879292
5.537114817087539
5.504591952060234
5.520689815202623
5.53399838044078
5.509020866851056
5.500838561973071
5.54948087158324
5.5331670347131405
5.527727218127986
5.547239785266977
5.509013529013254
5.530309905185032
5.505490263798005
5.516950702468217
5.5190091151510305
5.535963921119606
5.508537431058913
5.515402076785705
5.515632458027361


x = list(range(20))
x
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

r.choice(x)
5
r.choice(x)
10
r.choice(x)
6


for i in range(20):
    print(r.choice(x))

    
1
7
12
9
3
18
15
10
7
6
6
18
18
2
0
16
2
13
11
5


s = "Paata mamporia"
s
'Paata mamporia'

r.choice(s)
'a'
r.choice(s)
'p'
r.choice(s)
'a'


mixed_s = ''
for i in range(len(s)):
    mixed_s += r.choice(s)

    
mixed_s
'aamoPPrParotPa'




= RESTART: D:/199/7_5/2023/simple_if_demo.py
enter an integer: 4
Hi even!

= RESTART: D:/199/7_5/2023/simple_if_demo.py
enter an integer: 10
Hi five!
Hi even!

= RESTART: D:/199/7_5/2023/simple_if_demo.py
enter an integer: 13
>>> 
= RESTART: D:/199/7_5/2023/simple_if_demo.py
enter an integer: 4
>>> 
>>> 
>>> x = r.randint(0, 1000)
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    x = r.randint(0, 1000)
NameError: name 'r' is not defined
>>> 
>>> 
>>> import random as r
>>> 
>>> x = r.randint(0, 1000)
>>> 
>>> if x % 2 == 0:
...     print("Even")
... else:
...     print("Odd")
... 
...     
Odd
>>> x
653
