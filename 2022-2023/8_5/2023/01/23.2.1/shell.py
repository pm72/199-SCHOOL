Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

=================== RESTART: D:/199/8_5/2023/addition_quiz.py ==================
What is 8 + 6? 14

== RESTART: D:/199/8_5/2023/addition_quiz.py ==
What is 5 + 9? 14
5 + 9 = 14 is True

== RESTART: D:/199/8_5/2023/addition_quiz.py ==
What is 0 + 5? 2
0 + 5 = 2 is False

== RESTART: D:/199/8_5/2023/addition_quiz.py ==
What is 7 + 5? 11
7 + 5 = 11 is False
7 + 5 = 12


import random as r

r.randint(0, 2)
1
r.randint(0, 2)
1
r.randint(0, 2)
2
r.randint(0, 2)
2
r.randint(0, 2)
0


r.randrange(5, 12)
5
r.randrange(5, 12)
5
r.randrange(5, 12)
6

for i in range(20):
    print(r.randrange(5, 12))

    
7
9
7
7
8
9
10
6
6
9
9
6
5
6
5
11
8
10
8
6


r.randrange(0, 1)
0
r.randrange(0, 1)
0
r.randrange(0, 1)
0
r.randrange(0, 1)
0


r.random()
0.42018606348549303
r.random()
0.28130303437229953



r.uniform(5.5, 5.55)
5.518148185895166


for i in range(30):
    print(r.uniform(5.5, 5.51))

    
5.509680058299709
5.50771734126283
5.502168376920492
5.506048896990842
5.509947195360458
5.50223754628454
5.502957186109804
5.504916621582147
5.504047402372933
5.5017330180246535
5.50857349918087
5.502804917954597
5.504711479193284
5.50917174442021
5.508294152010017
5.503419124716111
5.500627963835718
5.508517250551739
5.509727903057655
5.502655911398771
5.506091499268325
5.500727439783873
5.5041046556067466
5.501307060879818
5.501119249333704
5.509335031717675
5.506026746989205
5.506621667641361
5.503904135175759
5.503593374279669



a = [15, 25, 21, 3, 0, -15, 21, True, None, "Paata", False]

r.choice(a)
15
r.choice(a)
21
r.choice(a)
21
r.choice(a)
21
r.choice(a)
21
r.choice(a)
-15
r.choice(a)
-15
r.choice(a)
0
r.choice(a)
r.choice(a)
15
r.choice(a)
False
r.choice(a) ** 2
225
r.choice(a) ** 2
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    r.choice(a) ** 2
TypeError: unsupported operand type(s) for ** or pow(): 'NoneType' and 'int'


x = r.choice(a)
if type(x) == int:
    print(x ** 2)
else:
    print("Not supported...")

    
441
True ** 2
1
False ** 3
0
 None ** 2
 
SyntaxError: unexpected indent
None ** 2
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    None ** 2
TypeError: unsupported operand type(s) for ** or pow(): 'NoneType' and 'int'


arr = [15, 25, 11, 0, 58, 12]
arr = [15, 25, 11, 0, 58, 12]
r.shuffle(arr)
arr
[58, 25, 11, 12, 15, 0]


name = "alexander"
r.shuffle(name)
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    r.shuffle(name)
  File "C:\Program Files\Python310\lib\random.py", line 394, in shuffle
    x[i], x[j] = x[j], x[i]
TypeError: 'str' object does not support item assignment

list(r.shuffle(name))
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    list(r.shuffle(name))
  File "C:\Program Files\Python310\lib\random.py", line 394, in shuffle
    x[i], x[j] = x[j], x[i]
TypeError: 'str' object does not support item assignment


n = r.shuffle(list(name))
n
n


name
'alexander'
name = list(name)
name
['a', 'l', 'e', 'x', 'a', 'n', 'd', 'e', 'r']

r.shuffle(name)
name
['a', 'e', 'r', 'e', 'n', 'd', 'x', 'a', 'l']

n = ''
n += str(i for i in name)
n
'<generator object <genexpr> at 0x0000028471CAAC70>'
str(n)
'<generator object <genexpr> at 0x0000028471CAAC70>'
*n
SyntaxError: can't use starred expression here
print(*n)
< g e n e r a t o r   o b j e c t   < g e n e x p r >   a t   0 x 0 0 0 0 0 2 8 4 7 1 C A A C 7 0 >

list(n)
['<', 'g', 'e', 'n', 'e', 'r', 'a', 't', 'o', 'r', ' ', 'o', 'b', 'j', 'e', 'c', 't', ' ', '<', 'g', 'e', 'n', 'e', 'x', 'p', 'r', '>', ' ', 'a', 't', ' ', '0', 'x', '0', '0', '0', '0', '0', '2', '8', '4', '7', '1', 'C', 'A', 'A', 'C', '7', '0', '>']

n = ''
name
['a', 'e', 'r', 'e', 'n', 'd', 'x', 'a', 'l']
for i in name:
    n += i

    
n
'aerendxal'

== RESTART: D:/199/8_5/2023/substracy_quiz.py =
What is 2 - 0? 2
2 - 0 = 2 is True
>>> 
== RESTART: D:/199/8_5/2023/substracy_quiz.py =
What is 7 - 7? 0
7 - 7 = 0 is True
7 - 7 = 0
>>> 
== RESTART: D:/199/8_5/2023/substracy_quiz.py =
What is 3 - 0? 2
3 - 0 = 2 is False
3 - 0 = 3
>>> 
>>> 
>>> 
>>> x = r.randint(1, 100)
>>> while x == 7:
...     x = r.randint(1, 100)
... 
...     
>>> x
21
