Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
===================== RESTART: D:\შემაჯამებელი 1\2_12.py =====================
a	b	a ** b
1	2	1
2	3	8
3	4	81
5	6	15625

>>> 
===================== RESTART: D:\შემაჯამებელი 1\2_12.py =====================
a    b    a ** b
1    2    1
2    3    8
3    4    81
5    6    15625

>>> 
===================== RESTART: D:\შემაჯამებელი 1\2_12.py =====================
a	b	a ** b
1	2	1
2	3	8
3	4	81
5	6	15625

>>> 
===================== RESTART: D:\შემაჯამებელი 1\2_12.py =====================
a	b	a ** b
1	2	1
>>> 
===================== RESTART: D:\შემაჯამებელი 1\2_12.py =====================
a	b	a ** b
1	2	1****
>>> 
>>> 
>>> 
>>> print(2+9)
11
>>> input()
hjkhjhj
'hjkhjhj'
>>> input("Enter a number:")
Enter a number:45
'45'
>>> 
>>> 
>>> a = input("Enter a number:")
Enter a number:25
>>> a
'25'
>>> a + 65
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    a + 65
TypeError: must be str, not int
>>> a = int(a)
>>> a + 65
90
>>> a
25
>>> a = int(input("Type an integer number: "))
Type an integer number: 23
>>> a
23
>>> int
<class 'int'>
>>> int()
0
>>> a = int(input("Type an integer number: "))
Type an integer number: 2.9
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    a = int(input("Type an integer number: "))
ValueError: invalid literal for int() with base 10: '2.9'
>>> a = float(input("Type an integer number: "))
Type an integer number: 25
>>> a
25.0
>>> a = eval(input("Type an integer number: "))
Type an integer number: 28
>>> a
28
>>> a = eval(input("Type an integer number: "))\

    
Type an integer number: 2.58
>>> a
2.58
>>> 
>>> 
>>> eval('2.58')
2.58
>>> eval('2.58.25')
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    eval('2.58.25')
  File "<string>", line 1
    2.58.25
          ^
SyntaxError: unexpected EOF while parsing
>>> eval('2.58, 25')
(2.58, 25)
>>> eval('paatra')
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    eval('paatra')
  File "<string>", line 1, in <module>
NameError: name 'paatra' is not defined
>>> 
>>> 
>>> celsius = eval(input("Enter celsius: "))
Enter celsius: 45
>>> print(celsius, "Ceslsius is", (9/5) * celsius + 32, "Fahrenheit")
45 Ceslsius is 113.0 Fahrenheit
>>> 
>>> celsius = eval(input("Enter celsius: "))
Enter celsius: 2.59
>>> print(celsius, "Ceslsius is", (9/5) * celsius + 32, "Fahrenheit")
2.59 Ceslsius is 36.662 Fahrenheit
>>> 
>>> 
>>> 
>>> x, y = 2.58, 3
>>> x
2.58
>>> y
3
>>> 
>>> 
>>> x, y = y,x
>>> x
3
>>> y
2.58
>>> a, b, c = 1, 2, 3
>>> a,b,c
(1, 2, 3)
>>> a, b, c = b, c, a
>>> a, b, c
(2, 3, 1)
>>> 
>>> 
>>> 
>>> orlando_x, orlando_y = eval(input("Enter coordinates:"))
Enter coordinates:-0.2599, 2.5899
>>> 
