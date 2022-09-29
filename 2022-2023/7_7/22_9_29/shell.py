Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> x = input()
25
>>> x
'25'
>>> x = eval(input("Enter a nummeric value: "))
Enter a nummeric value: 2.14
>>> x
2.14
>>> type(x)
<class 'float'>
>>> x = eval(input("Enter a nummeric value: "))
Enter a nummeric value: 25
>>> x
25
>>> type(x)
<class 'int'>
>>> 
============ RESTART: D:/199/7_7/22.9.29/საშუალო არითმეტიკული.py ============
Enter number1: 1
Enter number2: 2
Enter number3: 3
The average of 1 2 3 is 2.0
>>> 
============ RESTART: D:/199/7_7/22.9.29/საშუალო არითმეტიკული.py ============
Enter number1: 2.56
Enter number2: 1.08
Enter number3: 0.91
The average of 2.56 1.08 0.91 is 1.5166666666666666
>>> 
============ RESTART: D:/199/7_7/22.9.29/საშუალო არითმეტიკული.py ============
Enter number1: 2.56
Enter number2: 1.08
Enter number3: 0.91
The average of 2.56 1.08 0.91 is 2
>>> 
============ RESTART: D:/199/7_7/22.9.29/საშუალო არითმეტიკული.py ============
Enter number1: 2.56
Enter number2: 1.08
Enter number3: 0.91
The average of 2.56 1.08 0.91 is 1.52
>>> 
>>> 
>>> average
1.5166666666666666
>>> 
>>> 
>>> 
>>> x = 20
>>> y = 15
>>> 
>>> 
>>> temp = x
>>> x = y
>>> y = temp
>>> 
>>> x, y
(15, 20)
>>> 
>>> 
>>> x = 20
>>> y = 15
>>> 
>>> x, y
(20, 15)
>>> 
>>> x, y = y, x
>>> x, y
(15, 20)
>>> 
>>> 
>>> a, b, = 1, 2
>>> a,b
(1, 2)
>>> 
>>> a, b = 1, 2, 3
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    a, b = 1, 2, 3
ValueError: too many values to unpack (expected 2)
>>> 
>>> a, b, c = 1, 2
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    a, b, c = 1, 2
ValueError: not enough values to unpack (expected 3, got 2)
>>> 
>>> a =1
>>> b = 2
>>> c =
SyntaxError: invalid syntax
>>> 
>>> 
>>> a, b, c = eval(input("Enter three numbers: "))
Enter three numbers: 1, 6, 2.98
>>> a, b, c
(1, 6, 2.98)
>>> 
============ RESTART: D:/199/7_7/22.9.29/საშუალო არითმეტიკული.py ============
Enter three numbers: 2, 9, 33
The average of 2 9 33 is 14.67
>>> 
============ RESTART: D:/199/7_7/22.9.29/საშუალო არითმეტიკული.py ============
Enter three numbers: 2 9 6
Traceback (most recent call last):
  File "D:/199/7_7/22.9.29/საშუალო არითმეტიკული.py", line 5, in <module>
    numb1, numb2, numb3 = eval(input("Enter three numbers: "))
  File "<string>", line 1
    2 9 6
      ^
SyntaxError: invalid syntax
>>> 
============ RESTART: D:/199/7_7/22.9.29/საშუალო არითმეტიკული.py ============
Enter three numbers separated by commas: 25, 36, 11
The average of 25 36 11 is 24.0
>>> 
>>> 
>>> 
>>> 5
5

>>> 
>>> 
>>> a = 5
>>> id(a)
1918687088
>>> id(5)
1918687088
>>> print(a)
5
>>> type(5)
<class 'int'>
>>> type(a)
<class 'int'>
>>> 
>>> from sys import getsizeof
>>> getsizeof(5)
14
>>> getsizeof(a)
14
>>> getsizeof('5')
26
>>> getsizeof(2.5)
16
>>> getsizeof(5 ** 25)
20
>>> 5 ** 25
298023223876953125
>>> 
