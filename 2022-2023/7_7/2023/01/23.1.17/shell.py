Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

============== RESTART: D:/199/7_7/2023/01/23.1.17/circle_area.py ==============
Enter radius: 2.89
the area is 26.24

===== RESTART: D:/199/7_7/2023/01/23.1.17/circle_area.py =====
Enter radius: -5
Wrong input, enter positive number!..


 a = 9
 
SyntaxError: unexpected indent

===== RESTART: D:/199/7_7/2023/01/23.1.17/circle_area.py =====
Enter radius: -89
Wrong input, enter positive number!..



#  >, >=, <, <=, ==, !=

a = 5
a
5

a == 5
True

a < 5
False
a <= 5
True

a > 5
False
a >= 5
True

a != 5
False


x = True
x
True

x + 5
6

False + 5
5


int(True)
1

int(False)
0


# bool, int, float, str

bool(1)
True
bool(1.0)
True
bool(28)
True
bool(-2.88)
True
bool(0)
False
bool(0.0)
False
bool("")
False
bool(" ")
True


a = 5
b = 3

a + b != a * b
True

a + (b != a) * b
8

a + (b == a) * b
5


if a:
    print("variable a not equal zero")

    
variable a not equal zero


if a == True:
    print("variable a not equal zero")

    
if bool(a) == True:
    print("variable a not equal zero")

    
variable a not equal zero


a = False
if a:
...     print("variable a not equal zero")
... 
...     
>>> 
===== RESTART: D:/199/7_7/2023/01/23.1.17/circle_area.py =====
Enter radius: 5.89
the area is 108.99
>>> 
===== RESTART: D:/199/7_7/2023/01/23.1.17/circle_area.py =====
Enter radius: -8
>>> 
>>> 
>>> 
>>> x = 11
>>> if x % 2 == 0:
...     print("Even")
... else:
...     print("Odd")
... 
...     
Odd
>>> 
>>> 
>>> if x % 2 == 0:
...     print("Even")
... 
...     
