Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 8/5
1.6
>>> 8 / 4
2.0
>>> 5 + 8 / 4
7.0
>>> 
>>> 5 + 1.0
6.0
>>> int(5 + 8 / 2)
9
>>> 
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
>>> s = 0
>>> s + 1
1
>>> s
0
>>> s = s + 1
>>> s
1
>>> s = s + 1
>>> s
2
>>> s += 1
>>> s
3
>>> s += 10
>>> s
13
>>> s -= 10
>>> s
3
>>> s * 5
15
>>> s
3
>>> s *= 5
>>> s
15
>>> s /= 5    # s = s / 5
>>> s
3.0
>>> s = 15
>>> s //= 5
>>> s
3
>>> s %= 8
>>> s
3
>>> s %= 3
>>> s
0
>>> s %= 7
>>> 
>>> s / 0
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    s / 0
ZeroDivisionError: division by zero
>>> 
>>> 
>>> 
>>> 3 % 8   # 3 // 8 = 0 0 +3
3
>>> 
>>> 
>>> 
>>> x = 45
>>> d1 = x % 10
>>> d1
5
>>> d2 = x // 10
>>> d2
4
>>> print(d1, d2)
5 4
>>> print(d1, d2, sep='')
54
>>> print(d1, d2)
5 4
>>> print(d1, d2, sep='****')
5****4
>>> 
>>> 
>>> x = 45
>>> reverse_x = x % 10 * 10 + x // 10 * 1
>>> reverse_x
54
>>> reverse_x * 5
270
>>> 
>>> 
>>> x = 528
>>> reverse_x = x % 10 * 100 + x // 10 % 10 * 10 + x // 100 *
SyntaxError: invalid syntax
>>> reverse_x = x % 10 * 100 + x // 10 % 10 * 10 + x // 100 * 1
>>> reverse_x
825
>>> reverse_x / 5
165.0
>>> 
============= RESTART: D:/199/7_3/22.10.05/შებრუნებული რიცხვი.py =============
Enter an integer number: 8593
Recverse number is 3958
>>> reverse_x // 2
1979
>>> 
============= RESTART: D:/199/7_3/22.10.05/შებრუნებული რიცხვი.py =============
Enter an integer number: 100100589
Reverse number is 985001001
>>> 
============= RESTART: D:/199/7_3/22.10.05/შებრუნებული რიცხვი.py =============
Enter an integer number: 100
Reverse number is 1
>>> 
