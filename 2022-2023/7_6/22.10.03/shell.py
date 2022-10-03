Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
=================== RESTART: D:\199\7_6\22.10.3\Average.py ===================
Enter a number1: 15
Enter a number2: 2.89
Enter a number3: 20
>>> numb1
15
>>> type(numb1)
<class 'int'>
>>> type(numb2)
<class 'float'>
>>> numb2
2.89
>>> type(numb3)
<class 'int'>
>>> 
>>> 
=================== RESTART: D:\199\7_6\22.10.3\Average.py ===================
Enter a number1: 1
Enter a number2: 2
Enter a number3: 3
The average of 1 2 3 is 2.0
>>> 
=================== RESTART: D:\199\7_6\22.10.3\Average.py ===================
Enter a number1: 0.98
Enter a number2: 2.34
Enter a number3: 1.57
The average of 0.98 2.34 1.57 is 1.63
>>> 
=================== RESTART: D:\199\7_6\22.10.3\Average.py ===================
Enter a number1: 1.658645
Enter a number2: 2.01455
Enter a number3: 3
The average of 1.658645 2.01455 3 is 2.22
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
>>> x, y
(20, 15)
>>> 
>>> x, y = y, x
>>> 
>>> x, y
(15, 20)
>>> 
>>> 
>>> X, Y = 1.256, 32
>>> X, Y
(1.256, 32)
>>> 
>>> 
>>> x, y = 7, 8, 9
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    x, y = 7, 8, 9
ValueError: too many values to unpack (expected 2)
>>> 
>>> 
>>> x, y, z = 4, 8
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    x, y, z = 4, 8
ValueError: not enough values to unpack (expected 3, got 2)
>>> 
>>> 
>>> a, b = input("Enter two numbers: ")
Enter two numbers: 14, 21
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    a, b = input("Enter two numbers: ")
ValueError: too many values to unpack (expected 2)
>>> a, b = eval*input("Enter two numbers: "))
SyntaxError: invalid syntax
>>> a, b = eval(input("Enter two numbers: "))
Enter two numbers: 15, 21
>>> a
15
>>> b
21
>>> 
=================== RESTART: D:\199\7_6\22.10.3\Average.py ===================
Enter a number1: 
=================== RESTART: D:\199\7_6\22.10.3\Average.py ===================
Enter three numbers: 25 36 21
Traceback (most recent call last):
  File "D:\199\7_6\22.10.3\Average.py", line 5, in <module>
    numb1, numb2, numb3 = eval(input("Enter three numbers: "))
  File "<string>", line 1
    25 36 21
        ^
SyntaxError: invalid syntax
>>> 
=================== RESTART: D:\199\7_6\22.10.3\Average.py ===================
Enter three numbers separated by commas: 21, 22, 54
The average of 21 22 54 is 32.33
>>> 
>>> 
>>> 
>>> 3 ** 2
9
>>> 22.5 **3
11390.625
>>> 2.5 ** 3
15.625
>>> 
>>> 
>>> 1.258 ** 3.69
2.3324995342170016
>>> 
>>> 
>>> 
>>> ? = 45
SyntaxError: invalid syntax
>>> 
>>> 
>>> x = 45
>>> s = x % 10 + x // 10
>>> s
9
>>> x % 10
5
>>> x // 10
4
>>> 
>>> 
>>> x = int(input("Enter an integer number: "))
Enter an integer number: 10
>>> x % 2
0
>>> x = int(input("Enter an integer number: "))
Enter an integer number: 11
>>> x % 2
1
>>> if x % 2 == 0 "even" else "odd"
SyntaxError: invalid syntax
>>> 
>>> [if x % 2 == 0 "even" else "odd"]
SyntaxError: invalid syntax
>>> print("even" if x % 2 == 0 else "odd")
odd
>>> x
11
>>> x = int(input("Enter an integer number: "))
Enter an integer number: 64
>>> print("even" if x % 2 == 0 else "odd")
even
>>> 
>>> 
