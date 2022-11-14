Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
============ RESTART: D:\199\7_3\22.10.03\საშუალო არითმეტიკული.py ============
Enter number1: 1
Enter number2: 2
Enter number3: 3
The average of 1 2 3 is 2.0
>>> 
============ RESTART: D:\199\7_3\22.10.03\საშუალო არითმეტიკული.py ============
Enter number1: 1.589
Enter number2: 0.369784
Enter number3: 0.00982
The average of 1.589 0.369784 0.00982 is 0.66
>>> 
>>> 
>>> x = 20
>>> y = 15
>>> 
>>> temp = x
>>> x = y
>>> y =  temp
>>> 
>>> x, y
(15, 20)
>>> 
>>> 
>>> x = 20
>>> y = 15
>>> x,y
(20, 15)
>>> 
>>> x, y = y, x
>>> x, y
(15, 20)
>>> 
>>> 
>>> x, y = 58, 1.56
>>> x, y
(58, 1.56)
>>> 
>>> x, y = 1, 2, 3
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    x, y = 1, 2, 3
ValueError: too many values to unpack (expected 2)
>>> 3
3
>>> 
>>> 
>>> x, y, z = 2, 50
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    x, y, z = 2, 50
ValueError: not enough values to unpack (expected 3, got 2)
>>> 
>>> 
>>> x, y = eval(input("Enter two numbers: "))
Enter two numbers: 5, 8
>>> x,y
(5, 8)
>>> x, y = eval(input("Enter two numbers: "))
Enter two numbers: 4, 7, 8
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    x, y = eval(input("Enter two numbers: "))
ValueError: too many values to unpack (expected 2)
>>> 
============ RESTART: D:\199\7_3\22.10.03\საშუალო არითმეტიკული.py ============
Enter three numbers: 25 69 33
Traceback (most recent call last):
  File "D:\199\7_3\22.10.03\საშუალო არითმეტიკული.py", line 5, in <module>
    numb1, numb2, numb3 = eval(input("Enter three numbers: "))
  File "<string>", line 1
    25 69 33
        ^
SyntaxError: invalid syntax
>>> 
============ RESTART: D:\199\7_3\22.10.03\საშუალო არითმეტიკული.py ============
Enter three numbers separated by commas: 25, 33, 1.58
The average of 25 33 1.58 is 19.86
>>> 
>>> numb1
25
>>> numb2
33
>>> numb3
1.58
>>> 
