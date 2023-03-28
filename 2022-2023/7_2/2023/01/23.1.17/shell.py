Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

============== RESTART: D:/199/7_2/2023/01/23.1.17/circle_area.py ==============
Enter a radius: -5
Wrong input, enter positive number.

==== RESTART: D:/199/7_2/2023/01/23.1.17/circle_area.py ===
Enter a radius: 5

==== RESTART: D:/199/7_2/2023/01/23.1.17/circle_area.py ===
Enter a radius: 5.89
The area is 108.99



 a = 9
 
SyntaxError: unexpected indent

==== RESTART: D:/199/7_2/2023/01/23.1.17/circle_area.py ===
Enter a radius: -5
Wrong input, enter positive number.
OK

==== RESTART: D:/199/7_2/2023/01/23.1.17/circle_area.py ===
Enter a radius: 2.21
The area is 15.34

==== RESTART: D:/199/7_2/2023/01/23.1.17/circle_area.py ===
Enter a radius: -5
Wrong input, enter positive number.
Traceback (most recent call last):
  File "D:/199/7_2/2023/01/23.1.17/circle_area.py", line 9, in <module>
    print(f"The area is {area:.2f}")
NameError: name 'area' is not defined

==== RESTART: D:/199/7_2/2023/01/23.1.17/circle_area.py ===
Enter a radius: -8
Wrong input, enter positive number.
The area is 0.00

==== RESTART: D:/199/7_2/2023/01/23.1.17/circle_area.py ===
Enter a radius: 2.68
The area is 22.56

==== RESTART: D:/199/7_2/2023/01/23.1.17/circle_area.py ===
Enter a radius: -8
The area is 0.00



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



#  int,  float,  str
# bool

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


bool(1)
True
bool(25)
True
bool(-2.5)
True
>>> bool(0)
False
>>> bool(0.0)
False
>>> bool("")
False
>>> bool(" ")
True
>>> 
>>> 
>>> a = 5
>>> if a:
...     print("Non zero")
... 
...     
Non zero
>>> 
>>> if a == True:
...     print("Non zero")
... 
...     
>>> 
>>> if bool(a) == True:
...     print("Non zero")
... 
...     
Non zero
