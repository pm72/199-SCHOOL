Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> x = 45
>>> # 4 * 10 + 5 * 1
>>> # 5 * 10 + 4 * 1
>>> d1 = x % 10
>>> d2 = x // 10
>>> 
>>> print(d1, d2)
5 4
>>> print(d1,d2)
5 4
>>> 
>>> help(print)
Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.

>>> 
>>> 
>>> print(d1, d2, sep='')
54
>>> 
>>> 
>>> x = 45
>>> reversed_x = d1 * 10 + d2 * 1
>>> reversed_x
54
>>> reversed_x * 5
270
>>> 
>>> 
>>> x = 571
>>> reversed_x = x % 10 * 100 + x // 10 % 10 * 10 + x // 100 * 1
>>> reversed_x
175
>>> reversed_x // 5
35
>>> reversed_x / 5
35.0
>>> 
>>> 
>>> 8 / 4
2.0
>>> 5 + 8 / 4
7.0
>>> 5 + 1.0
6.0
>>> 
>>> 
>>> int(5 + 8 / 4)
7
>>> 
>>> 
============ RESTART: D:/199/8_4/22.10.07/შეტრიალებული რიცხვი.py ============
Enter an integer: 46565658989
Reversed number is 0
>>> 
============ RESTART: D:/199/8_4/22.10.07/შეტრიალებული რიცხვი.py ============
Enter an integer: 8593
Reversed number is 0
>>> 
============ RESTART: D:/199/8_4/22.10.07/შეტრიალებული რიცხვი.py ============
Enter an integer: 8593
Reversed number is 3958
>>> reversed_x / 2
1979.0
>>> 
============ RESTART: D:/199/8_4/22.10.07/შეტრიალებული რიცხვი.py ============
Enter an integer: 587412589514
Reversed number is 415985214785
>>> 
============ RESTART: D:/199/8_4/22.10.07/შეტრიალებული რიცხვი.py ============
Enter an integer: 5
Reversed number is 5
>>> 
============ RESTART: D:/199/8_4/22.10.07/შეტრიალებული რიცხვი.py ============
Enter an integer: 100
Reversed number is 1
>>> 
============ RESTART: D:/199/8_4/22.10.07/შეტრიალებული რიცხვი.py ============
Enter an integer: 1002
Reversed number is 2001
>>> 
============ RESTART: D:/199/8_4/22.10.07/შეტრიალებული რიცხვი.py ============
Enter an integer: 1001
Reversed number is 1001
>>> 
============ RESTART: D:/199/8_4/22.10.07/შეტრიალებული რიცხვი.py ============
Enter an integer: 5458847554646489448948941256
Reversed number is 6521498498449846464557488545
>>> 
