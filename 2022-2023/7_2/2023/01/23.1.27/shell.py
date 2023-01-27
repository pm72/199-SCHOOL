Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

=================== RESTART: D:/199/7_2/2023/addition_quiz.py ==================
What is 4 + 7? 11

=== RESTART: D:/199/7_2/2023/addition_quiz.py ==
What is 2 + 5? 7
2 + 5 = 7 is True

=== RESTART: D:/199/7_2/2023/addition_quiz.py ==
What is 8 + 9? 12
8 + 9 = 12 is False

=== RESTART: D:/199/7_2/2023/addition_quiz.py ==
What is 1 + 3? 5
1 + 3 = 5 is False
1 + 3 is 4

=== RESTART: D:/199/7_2/2023/addition_quiz.py ==
What is 8 + 1? 9
8 + 1 = 9 is True



import random as r

r.randint(0, 5)
5


r.randint(0, 5)
4
r.randint(0, 5)
0
r.randint(0, 5)
0
r.randint(0, 5)
3

r.randrange(0, 8)
2
r.randrange(0, 8)
1
r.randrange(0, 8)
6

r.randrange(0, 1)
0
r.randrange(0, 1)
0
r.randrange(0, 1)
0


r.random()
0.8849766366740502
r.random()
0.3280742100418498
r.random()
0.7158083862640774

r.uniform(7, 7.24)
7.208263054698793
r.uniform(7, 7.24)
7.179080162410503
r.uniform(7, 7.24)
7.086167302430858
r.uniform(7, 7.24)
7.076064915695466


r.uniform(7, 7.0001)
7.000027568009459
r.uniform(7, 7.0001)
7.000028183179696
r.uniform(7, 7.0001)
7.000011394872591
r.uniform(7, 7.0001)
7.000085402445423


for i in range(20):
    print(r.uniform(7, 7.0001))

    
7.000065252001643
7.000086794675057
7.000073055276069
7.00007318048677
7.000033252640824
7.000045529919484
7.000048374316978
7.000005543104137
7.000034893598225
7.000019985642452
7.000007252733664
7.000089174368645
7.000080914911296
7.000035643310307
7.000048424049077
7.0000965649566265
7.000064398729446
7.000082089805044
7.000023031946326
7.000042961831405


a = range(1, 60)
print(*a)
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59

r.choice(a)
54
r.choice(a)
59
r.choice(a)
29
r.choice(a)
22


names = ["Paata", "Tamuna", "Dodo", "Lia", "Gio", "Nana", "Emzari"]

r.choce(names)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    r.choce(names)
AttributeError: module 'random' has no attribute 'choce'. Did you mean: 'choice'?

r.choice(names)
'Emzari'
r.choice(names)
'Nana'
r.choice(names)
'Lia'

name = 'Teona'
name == r.choice(names)
False

names.append('Teona')

name == r.choice(names)
False
name == r.choice(names)
False
name == r.choice(names)
False
name == r.choice(names)
False
name == r.choice(names)
False
name == r.choice(names)
False
name == r.choice(names)
False


for i in range(20):
    print(name == r.choice(names))

    
True
False
False
False
False
True
True
True
False
False
False
False
False
False
False
False
False
False
False
False



*names
SyntaxError: can't use starred expression here


names
['Paata', 'Tamuna', 'Dodo', 'Lia', 'Gio', 'Nana', 'Emzari', 'Teona']



== RESTART: D:/199/7_2/2023/simple_tf_demo.py ==
Enter an integer: 12
Hi even!

== RESTART: D:/199/7_2/2023/simple_tf_demo.py ==
Enter an integer: 10
Hi five!
Hi even!

== RESTART: D:/199/7_2/2023/simple_tf_demo.py ==
Enter an integer: 21



not True
False

not False
True


not 5
False

not -5.2558
False

not 0
True

== RESTART: D:/199/7_2/2023/simple_tf_demo.py ==
Enter an integer: 5


x = 5
x % 2
1
not x % 2
False


not 10 % 2
True

== RESTART: D:/199/7_2/2023/simple_tf_demo.py ==
Enter an integer: 4
Even


>>> a = None
>>> a
>>> print(a)
None
>>> 
>>> a += 1
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    a += 1
TypeError: unsupported operand type(s) for +=: 'NoneType' and 'int'
>>> 
>>> 
>>> a = 90
>>> 
>>> a
90
>>> 
>>> not None
True
>>> not not None
False
>>> 
>>> bool(None)
False
