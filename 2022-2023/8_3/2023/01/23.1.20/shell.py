Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

============== RESTART: D:/199/8_3/2023/01/23.1.20/circle_area.py ==============
Enter a radius: -8
Wrong input. Enter a positive number.

== RESTART: D:/199/8_3/2023/01/23.1.20/circle_area.py =
Enter a radius: 2.56

== RESTART: D:/199/8_3/2023/01/23.1.20/circle_area.py =
Enter a radius: 2.58
The area is 20.9116973393551

== RESTART: D:/199/8_3/2023/01/23.1.20/circle_area.py =
Enter a radius: 2.58
The area is 20.91


 a = 6
 
SyntaxError: unexpected indent

== RESTART: D:/199/8_3/2023/01/23.1.20/circle_area.py =
Enter a radius: 9.54
The area is 285.92

== RESTART: D:/199/8_3/2023/01/23.1.20/circle_area.py =
Enter a radius: -1
Wrong input. Enter a positive number.
Traceback (most recent call last):
  File "D:/199/8_3/2023/01/23.1.20/circle_area.py", line 9, in <module>
    print(f"The area is {area:.2f}")
NameError: name 'area' is not defined

== RESTART: D:/199/8_3/2023/01/23.1.20/circle_area.py =
Enter a radius: 1.65
The area is 8.55

== RESTART: D:/199/8_3/2023/01/23.1.20/circle_area.py =
Enter a radius: -5

== RESTART: D:/199/8_3/2023/01/23.1.20/circle_area.py =
Enter a radius: -5
Enter a radius: -9
Enter a radius: 2
The area is 12.57

== RESTART: D:/199/8_3/2023/01/23.1.20/circle_area.py =
Enter a radius: -14
Enter a radius: 0
The area is 0.00

== RESTART: D:/199/8_3/2023/01/23.1.20/circle_area.py =
Enter a radius: 2.36.
Traceback (most recent call last):
  File "D:/199/8_3/2023/01/23.1.20/circle_area.py", line 6, in <module>
    r = eval(input("Enter a radius: "))
  File "<string>", line 1
    2.36.
SyntaxError: invalid syntax



# >, >=, <, <=, == , !=

a = 5
a
5

a == 5
True
a != 5
False

# int, float, str
# bool  ==>  True,  False

a = 5
b = 3

a + b != a * b
True

a + (b != a) * b
8


x = True
x
True

x + 5
6

a + True * b
8


int(2.59)
2

int(True)
1

int(False)
0


bool(0)
False
bool(0.0)
False
bool("")
False

bool(1)
True

bool(1.25)
True
>>> 
>>> bool(-0.5)
True
>>> 
>>> 
>>> a = 3
>>> if a:
...     print("Not equal zero")
... 
...     
Not equal zero
>>> 
>>> 
>>> if a == True:
...     print("OK")
... 
...     
>>> 
>>> if bool(a) == True:
...     print("OK")
... 
...     
OK
>>> 
