Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> x = 528
>>> print(x % 10 + x // 10 % 10, x // 100)
10 5
>>> print(x % 10 + x // 10 % 10 + x // 100)
15
>>> x = 100
>>> print(x % 10 + x // 10 % 10 + x // 100)
1
>>> x = 8
>>> print(x % 10 + x // 10 % 10 + x // 100)
8
>>> 
>>> 
>>> 
>>> x, y = 1, 2
>>> x, y
(1, 2)
>>> 
>>> v, a = eval(input("Enter speed and acceleration: "))
Enter speed and acceleration: 60, 3.5       # v, a = 60, 3.5
>>> length = (v ** 2) / (2 * a)
>>> 
>>> print("The minimum runway length for this airplane is", length, "meters")
The minimum runway length for this airplane is 514.2857142857143 meters
>>> print("The minimum runway length for this airplane is", round(length, 3), "meters")
The minimum runway length for this airplane is 514.286 meters
>>> 
>>> 
>>> 
>>> s = "a    b    a ** b\n"
>>> s += "1    2    1\n"
>>> s += "2    3    8\n"
>>> s += "3    4    81\n"
>>> s += "4    5    1024\n"
>>> s += "5    6    15625"
>>> 
>>> print(s)
a    b    a ** b
1    2    1
2    3    8
3    4    81
4    5    1024
5    6    15625
>>> 
>>> 
>>> 
>>> x1, y1, x2, y2, x3, y3 = 1.5, -3.4, 4.6, 5, 9.5, -3.4
>>> 
>>> a = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
>>> b = ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5
>>> c = ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0.5
>>> 
>>> p = (a + b + c) / 2
>>> 
>>> s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
>>> 
>>> print("The area of the triangle is", round(s, 2))
The area of the triangle is 33.6
>>> 
>>> 
>>> 
>>> 
