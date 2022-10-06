Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> eval('2.58')
2.58
>>> eval('46')
46
>>> '45' + '21'
'4521'
>>> eval('46') + 21
67
>>> input("number1: ")
number1: 25
'25'
>>> eval(input("number1: "))
number1: 25
25
>>> eval(input("number1: "))
number1: 2.56
2.56
>>> 
============ RESTART: D:/199/7_4/22.9.29/საშუალო არითმეტიკული.py ============
Enter the first number: 1
Enter the second number: 2
Enter the three number: 3
The average of 1 2 3 is 2.0
>>> 
============ RESTART: D:/199/7_4/22.9.29/საშუალო არითმეტიკული.py ============
Enter the first number: 25
Enter the second number: 1.69
Enter the three number: 032
Traceback (most recent call last):
  File "D:/199/7_4/22.9.29/საშუალო არითმეტიკული.py", line 3, in <module>
    number3 = eval(input("Enter the three number: "))
  File "<string>", line 1
    032
      ^
SyntaxError: invalid token
>>> 
============ RESTART: D:/199/7_4/22.9.29/საშუალო არითმეტიკული.py ============
Enter the first number: 
25
Enter the second number: 3.56
Enter the three number: 0.32
The average of 25 3.56 0.32 is 9.626666666666667
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
>>> x
15
>>> y
20
>>> x, y = 5, 9
>>> x
5
>>> y
9
>>> x, y = 5, 9, 12
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    x, y = 5, 9, 12
ValueError: too many values to unpack (expected 2)
>>> 
>>> 
>>> x,l y, z = 12, 89
SyntaxError: invalid syntax
>>> 
>>> 
>>> x, y, z = 12, 89
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    x, y, z = 12, 89
ValueError: not enough values to unpack (expected 3, got 2)
>>> x = 12
>>> y = 89
>>> z =
SyntaxError: invalid syntax
>>> 
>>> 
>>> x, y, z = input("Enter three values")
Enter three values25, 56, 36
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    x, y, z = input("Enter three values")
ValueError: too many values to unpack (expected 3)
>>> 25, 56, 36
(25, 56, 36)
>>> 
>>> 
>>> x, y, z = input("Enter three values: ")
Enter three values: 25, 36, 21
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    x, y, z = input("Enter three values: ")
ValueError: too many values to unpack (expected 3)
>>> 
>>> 
>>> 
============ RESTART: D:/199/7_4/22.9.29/საშუალო არითმეტიკული.py ============
Enter three numbers: 25, 36, 21
The average of 25 36 21 is 27.333333333333332
>>> 
>>> 
>>> x, y, z = eval(input("Enter three values: "))
Enter three values: 25, 56, 11
>>> x
25
>>> y
56
>>> z
11
>>> x, y, z = 15, 25, 66
>>> 
============ RESTART: D:/199/7_4/22.9.29/საშუალო არითმეტიკული.py ============
Enter the three numbers separated by commas: 25, 12, 33
The average of 25 12 33 is 23.333333333333332
>>> 
>>> 
>>> 
>>> "მინიჭების ოპერატორი"
'მინიჭების ოპერატორი'
>>> 
>>> X = 12
>>> x = 12
>>> 
>>> 
>>> x
12
>>> type(x)
<class 'int'>
>>> id(x)
1918687200
>>> id(12)
1918687200
>>> x
12
>>> import sys
>>> sys.getsizeof(12)
14
>>> sys.getsizeof(x)
14
>>> 
>>> 
>>> y = 25
>>> 
>>> x = y + 2
>>> x
27
>>> x = x + 3
>>> x
30
>>> x = x + (2*y + y/5)
>>> x
85.0
>>> 
>>> 
>>> 
>>> ''''''
''
>>> 
