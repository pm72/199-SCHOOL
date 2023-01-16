Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

================= RESTART: D:/199/8_4/2023/01/23.1.16/circle.py ================
Enter a radius: 15.89
The are is 793.2273264494595

================= RESTART: D:/199/8_4/2023/01/23.1.16/circle.py ================
Enter a radius: -5
Error! Enter a positive number...

================= RESTART: D:/199/8_4/2023/01/23.1.16/circle.py ================
Enter a radius: 0
The are is 0.0

================= RESTART: D:/199/8_4/2023/01/23.1.16/circle.py ================
Enter a radius: 15.89
The are is 793.23



#  <, <=, >, >=, ==, !=

a = 5
a == 5
True

b > 5
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    b > 5
NameError: name 'b' is not defined

b = 3
b > 5
False

a + b != a * b
True



x = 11
if x % 2 == 0:
    print("Even")
else:
    print("Odd")

    
Odd



x = 0

bool(x)
False

if x:
    print("positive")

    
#  if .. else

if x == True:
    print("Positive")

    
x
0


x = 1001
if x:
    print("Positive")

    
Positive

x = -1001
if x:
    print("Positive")

    
Positive


r = True

r + 5
6

int(True)
1
int(False)
0

True + 5
6

False + 6
6


r = 2 != 5
r
True



import random as r
r.randint(0, 9)
7
r.randint(0, 9)
9
r.randint(0, 9)
5
r.randint(0, 9)
5
r.randint(0, 9)
1

r.random()
0.45055044615708595
r.random()
0.6261038464736213
r.random()
0.4871123355973118

r.uniform(2, 3)
2.115657667177423
r.uniform(2, 3)
2.4006038675140706
r.uniform(2, 3)
2.034263818980463
>>> r.uniform(2, 3)
2.384334775556546
>>> 
>>> 
>>> n1 = r.randint(0, 9)
>>> n2 = r.randint(0, 9)
>>> 
>>> answer = eval(input(f"What is {n1} + {n2}"))
What is 7 + 3
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    answer = eval(input(f"What is {n1} + {n2}"))
  File "<string>", line 0
    
SyntaxError: invalid syntax
>>> 
>>> answer = eval(input(f"What is {n1} + {n2}? "))
What is 7 + 3? 10
>>> 
>>> if answer == n1 + n2:
...     print("True")
... else:
...     print("False")
... 
...     
True
