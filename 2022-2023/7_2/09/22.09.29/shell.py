Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
============ RESTART: D:/199/7_2/22.9.29/საშუალო არითმეტიკული.py ============
Enter number1: 1
Enter number2: 2
Enter number3: 3
The average of 1 2 3 is 2.0
>>> 
============ RESTART: D:/199/7_2/22.9.29/საშუალო არითმეტიკული.py ============
Enter number1: 25
Enter number2: 31
Enter number3: 2.89
The average of 25 31 2.89 is 19.63
>>> 
============ RESTART: D:/199/7_2/22.9.29/საშუალო არითმეტიკული.py ============
Enter number1: 22
Enter number2: 67
Enter number3: 19
The average of 22 67 19 is 36.0
>>> 
============ RESTART: D:/199/7_2/22.9.29/საშუალო არითმეტიკული.py ============
Enter number1: 1.25
Enter number2: 0.369
Enter number3: 2.89
The average of 1.25 0.369 2.89 is 1.5030000000000001
>>> 
============ RESTART: D:/199/7_2/22.9.29/საშუალო არითმეტიკული.py ============
Enter number1: 1.789214
Enter number2: 0.259
Enter number3: 3.69
The average of 1.789214 0.259 3.69 is 1.91
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
>>> 
>>> x = 20
>>> y = 15
>>> 
>>> x, y = y, x
>>> x, y
(15, 20)
>>> 
>>> 
>>> a, b = 1, 8
>>> a, b
(1, 8)
>>> 
>>> a, b = 2, 4, 6
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    a, b = 2, 4, 6
ValueError: too many values to unpack (expected 2)
>>> 

>>> a, b, c = 2, 8
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    a, b, c = 2, 8
ValueError: not enough values to unpack (expected 3, got 2)
>>> 
>>> 
>>> a, b = 4, 8
>>> a, b
(4, 8)
>>> 
>>> 
>>> a, b = input("Enter two values: ")
Enter two values: 5, 8
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    a, b = input("Enter two values: ")
ValueError: too many values to unpack (expected 2)
>>> 
>>> a, b = eval(input("Enter two values: "))
Enter two values: 5, 2
>>> a, b
(5, 2)
>>> a, b = input("Enter two values: ")
Enter two values: paata, eka
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    a, b = input("Enter two values: ")
ValueError: too many values to unpack (expected 2)
>>> a, b = input("Enter two values: ")
Enter two values: 'paata', 'teo'
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    a, b = input("Enter two values: ")
ValueError: too many values to unpack (expected 2)
>>> 
============ RESTART: D:/199/7_2/22.9.29/საშუალო არითმეტიკული.py ============
Enter three numbers: 20, 25, 11
The average of 20 25 11 is 18.67
>>> 
============ RESTART: D:/199/7_2/22.9.29/საშუალო არითმეტიკული.py ============
Enter three numbers: 25 21 33
Traceback (most recent call last):
  File "D:/199/7_2/22.9.29/საშუალო არითმეტიკული.py", line 5, in <module>
    numb1, numb2, numb3 = eval(input("Enter three numbers: "))
  File "<string>", line 1
    25 21 33
        ^
SyntaxError: invalid syntax
>>> 
============ RESTART: D:/199/7_2/22.9.29/საშუალო არითმეტიკული.py ============
Enter three numbers separated by commas: 12, 0, 3
The average of 12 0 3 is 5.0
>>> 
============ RESTART: D:/199/7_2/22.9.29/საშუალო არითმეტიკული.py ============
Enter three numbers separated by commas: 0,0,0
The average of 0 0 0 is 0.0
>>> 
>>> 
>>> 
>>> a = 5
>>> id(a)
1918687088
>>> id(5)
1918687088
>>> a
5
>>> mariami = 5
>>> id(mariami)
1918687088
>>> 
>>> type(a)
<class 'int'>
>>> 
>>> 
>>> import sys
>>> sys.getsizeof(a)
14
>>> sys.getsizeof(5)
14
>>> sys.getsizeof(5**25)
20
>>> 2**25
33554432
>>> 5 ** 25
298023223876953125
>>> 
>>> 
>>> 
>>> 
