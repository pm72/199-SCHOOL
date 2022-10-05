Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> x, y, z = 1, 2, 3
>>> x, y, z
(1, 2, 3)
>>> 
>>> x, y, z = eval(input("Enter three numbers: "))
Enter three numbers: 56, 21, 0
>>> x, y, z
(56, 21, 0)
>>> x, y, z = eval(input("Enter three numbers: "))
Enter three numbers: 25 63 21
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    x, y, z = eval(input("Enter three numbers: "))
  File "<string>", line 1
    25 63 21
        ^
SyntaxError: invalid syntax
>>> x, y, z = eval(input("Enter three numbers separated by commas: "))
Enter three numbers separated by commas: 0,0,0
>>> x, y, z
(0, 0, 0)
>>> 
>>> 
>>> 8 / 5
1.6
>>> 8 / 4
2.0
>>> 16 // 3
5
>>> 29 % 7
1
>>> 
>>> 
>>> 5 + 8 / 4
7.0
>>> 5 + 2.0
7.0
>>> 
>>> 
>>> int(5 + 2.0)
7
>>> 

>>> 
>>> x = 85
>>> d1 = x % 10
>>> d2 = x // 10
>>> print(d1, d2)
5 8
>>> print(d1, d2, sep='')
58
>>> revers_x = d1 * 10 + d2
>>> _
7
>>> reverse_x
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    reverse_x
NameError: name 'reverse_x' is not defined
>>> revers_x
58
>>> revers_x * 10
580
>>> 
>>> print(15, 25, 35, sep='')
152535
>>> 
>>> 
>>> x = 0
>>> x = x + 1
>>> x
1
>>> x += 1
>>> x
2
>>> x *= 7
>>> x
14
>>> x /= 7
>>> x
2.0
>>> x //= 1
>>> x
2.0
>>> 
=============== RESTART: D:/199/8_6/22.10.04/reverse_number.py ===============
Enter an integer number: 4832
2384
>>> 
=============== RESTART: D:/199/8_6/22.10.04/reverse_number.py ===============
Enter an integer number: 4832
2384
23840
>>> 
=============== RESTART: D:/199/8_6/22.10.04/reverse_number.py ===============
Enter an integer number: 4832
2384
23840
>>> 
=============== RESTART: D:/199/8_6/22.10.04/reverse_number.py ===============
Enter an integer number: 2
2
20
>>> 
=============== RESTART: D:/199/8_6/22.10.04/reverse_number.py ===============
Enter an integer number: 15874120
2147851
21478510
>>> 
=============== RESTART: D:/199/8_6/22.10.04/reverse_number.py ===============
Enter an integer number: 5.7
Traceback (most recent call last):
  File "D:/199/8_6/22.10.04/reverse_number.py", line 1, in <module>
    numb = int(input("Enter an integer number: "))   # 4832
ValueError: invalid literal for int() with base 10: '5.7'
>>> 
