Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
=========== RESTART: D:\199\7_1\22.9.30\წრის ფართობის გამოთვლა.py ===========
Entrer radius: 25.69
Traceback (most recent call last):
  File "D:\199\7_1\22.9.30\წრის ფართობის გამოთვლა.py", line 11, in <module>
    area = PI * radius ** 2
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
>>> radius
'25.69'
>>> type(radius)
<class 'str'>
>>> 
>>> 
>>> int('15')
15
>>> int('15.25')
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int('15.25')
ValueError: invalid literal for int() with base 10: '15.25'
>>> int(15.23)
15
>>> int(15.93)
15
>>> float('25.369')
25.369
>>> float('12')
12.0
>>> 
>>> float*(25)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    float*(25)
TypeError: unsupported operand type(s) for *: 'type' and 'int'
>>> float(25)
25.0
>>> eval('17')
17
>>> eval('17.025')
17.025
>>> eval(17.025)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    eval(17.025)
TypeError: eval() arg 1 must be a string, bytes or code object
>>> 
=========== RESTART: D:\199\7_1\22.9.30\წრის ფართობის გამოთვლა.py ===========
Entrer radius: 20
The area of the circle is 1256.64 of radius 20
The perimeter of the circle is 125.66 of radius 20

=========== RESTART: D:\199\7_1\22.9.30\წრის ფართობის გამოთვლა.py ===========
Entrer radius: 2.36
The area of the circle is 17.5 of radius 2.36
The perimeter of the circle is 14.83 of radius 2.36

=========== RESTART: D:\199\7_1\22.9.30\წრის ფართობის გამოთვლა.py ===========
Enter the radius: 22
The area of the circle is 1520.53 of radius 22
The perimeter of the circle is 138.23 of radius 22

>>> 
============ RESTART: D:/199/7_1/22.9.30/საშუალო არითმეტიკული.py ============
Enter number 1: 1
Enter number 2: 2
Enter number 3: 3
The average of 1 2 3 is 2.0
>>> type(average)
<class 'float'>
>>> 
>>> 
>>> 
>>> x = 20
>>> y = 15
>>> 
>>> temp = x
>>> x = y
>>> y = temp
>>> 
>>> x, y
(15, 20)
>>> 
