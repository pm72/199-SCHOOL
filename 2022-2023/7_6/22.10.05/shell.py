Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> s = 0
>>> 
>>> s + 1
1
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
>>> s*=5
>>> s
15
>>> s /= 5
>>> s
3.0
>>> 
>>> s = 15
>>> 
>>> s //= 5
>>> s
3
>>> s %= 5
>>> 3 %= 3
SyntaxError: can't assign to literal
>>> s %= 3
>>> s
0
>>> s %= 8
>>> s
0
>>> 
>>> 
>>> 
>>> x = 45
>>> d1 = x % 10
>>> d1
5
>>> d2 = x // 10
>>> 
>>> print(d1, d2)
5 4
>>> print(d1,       d2)
5 4
>>> print(d1, d2, sep='')
54
>>> print(d1, d2, sep='', end='')
54
>>> 
============= RESTART: D:/199/7_6/22.10.05/მარტივი არითმეტიკა.py =============
1415Paata
>>> 
============= RESTART: D:/199/7_6/22.10.05/მარტივი არითმეტიკა.py =============
1415Paata
Mamporia
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
>>> x = 549
>>> reverse_x = x % 10 * 100 + x // 10 % 10 * 10 + x // 100 * 1
>>> reverse_x
945
>>> 
>>> 
>>> 
