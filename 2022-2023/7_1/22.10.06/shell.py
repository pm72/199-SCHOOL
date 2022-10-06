Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> x = 20
>>> y = 15
>>> 
>>> t = x
>>> x = y
>>> y = t
>>> 
>>> x, y
(15, 20)
>>> 
>>> 
>>> x = 20
>>> y = 15
>>> 
>>> x, y = y, x
>>> x,y
(15, 20)
>>> 
>>> 
>>> x, y = 85, 21
>>> x,y
(85, 21)
>>> x, y = 15, 25, 9
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    x, y = 15, 25, 9
ValueError: too many values to unpack (expected 2)
>>> 
>>> x, y, z = 15, 21
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    x, y, z = 15, 21
ValueError: not enough values to unpack (expected 3, got 2)
>>> z =
SyntaxError: invalid syntax
>>> 
>>> 
>>> x, y, z = eval(input("Enter three numbers"))
Enter three numbers25, 36, 21
>>> x
25
>>> y
36
>>> z
21
>>> x, y, z = eval(input("Enter three numbers: "))
Enter three numbers: 25 36 21
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    x, y, z = eval(input("Enter three numbers: "))
  File "<string>", line 1
    25 36 21
        ^
SyntaxError: invalid syntax
>>> 
>>> x, y, z = eval(input("Enter three numbers separated by commas: "))
Enter three numbers separated by commas: 1.26, 3.025, 0
>>> x, y, z
(1.26, 3.025, 0)
>>> 
============ RESTART: D:\199\7_1\22.10.06\საშუალო არითმეტიკული.py ============
Enter three numbers separated by commas: 2, 3, 4
The average of 2 3 4 is 3.0
375.0
>>> 
>>> 
>>> 
>>> 8 / 5
1.6
>>> 8/4
2.0
>>> 5 + 8 / 4
7.0
>>> 
>>> 5 + 1.0
6.0
>>> 
>>> int(5 + 8 / 4)
7
>>> 2.5 * 1.56
3.9000000000000004
>>> 2.0 * 4.0
8.0
>>> 2.0 * 5
10.0
>>> -5
-5
>>> -5 * 9
-45
>>> 5 * -5
-25
>>> -5 * -5
25
>>> 8 // 5
1
>>> 19 // 6
3
>>> 
>>> 8 % 3
2
>>> 29 % 6
5
>>> 
>>> 
>>> 
