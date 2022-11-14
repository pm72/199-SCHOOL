Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
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
>>> x = 854
>>> reverse_x = x % 10 * 100 + x // 10 % 10 * 10 + x // 100 * 1
>>> 
>>> reverse_x
458
>>> reverse_x * 12
5496
>>> 
>>> 
>>> s = 0
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
>>> s *= 5
>>> s
15
>>> s /= 5
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
>>> s
0
>>> s += 1
>>> s = s + 1
>>> 
============= RESTART: D:/199/8_5/22.10.06/შებრუნებული რიცხვი.py =============
Enter an integer: 8593
Reversed number is 0
>>> 
============= RESTART: D:/199/8_5/22.10.06/შებრუნებული რიცხვი.py =============
Enter an integer: 8593
Reversed number is 3958
>>> 
============= RESTART: D:/199/8_5/22.10.06/შებრუნებული რიცხვი.py =============
Enter an integer: 100369
Reversed number is 963001
>>> 
============= RESTART: D:/199/8_5/22.10.06/შებრუნებული რიცხვი.py =============
Enter an integer: 100
Reversed number is 1
>>> 
============= RESTART: D:/199/8_5/22.10.06/შებრუნებული რიცხვი.py =============
Enter an integer: 25
Reversed number is 52
>>> 
============= RESTART: D:/199/8_5/22.10.06/შებრუნებული რიცხვი.py =============
Enter an integer: 8
Reversed number is 8
>>> 
============= RESTART: D:/199/8_5/22.10.06/შებრუნებული რიცხვი.py =============
Enter an integer: 1001001
Reversed number is 1001001
>>> 
============= RESTART: D:/199/8_5/22.10.06/შებრუნებული რიცხვი.py =============
Enter an integer: 703
Reversed number is 307
>>> reversed_x
307
>>> reversed_x * 10
3070
>>> 
