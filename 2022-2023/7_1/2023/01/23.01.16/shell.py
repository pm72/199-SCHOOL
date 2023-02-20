Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
============== RESTART: D:/199/7_1/2023/01/23.1.16/circle area.py ==============
Enter a radius: 15.89
The area of the circle is 793.23
>>> 
= RESTART: D:/199/7_1/2023/01/23.1.16/circle area.py
Enter a radius: -5
ERROR! Enter a positive number!
Negative
>>> 
= RESTART: D:/199/7_1/2023/01/23.1.16/circle area.py
Enter a radius: 0
The area of the circle is 0.00
>>> 
>>> 
>>> # <, <=, >, >=, ==, !=
>>> 
>>> a = 5
>>> a == 5
True
>>> 
>>> 
>>> b > 5
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    b > 5
NameError: name 'b' is not defined

b = 3
b > 5
False


a + b != a * b
True


x = True
x
True

x + 5
6
False + 5
5

int(False)
0
int(True)
1

bool(25)
True
bool(-2.5)
True
bool(0)
False
bool(0.0000)
False
bool("")
False
bool(" ")
True

x = 15
if x == True:
    print("Not equal zero")

    
if x == True:
    print("Not equal zero")

    
if x:
    print("Not equal zero")

    
Not equal zero


if bool(x) == True:
    print("Not equal zero")

    
Not equal zero


x = 0
if x:
    print("Not equal zero")

    

x = 11
if x % 2 == 0:
    print("Even")
else:
    print("Odd")

    
Odd
