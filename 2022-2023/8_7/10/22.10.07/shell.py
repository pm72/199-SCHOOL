Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> x = 45
>>> # 4 * 10 + 5 * 1
>>> # 5 * 10 + 4 * 1
>>> 
>>> d1 = x % 10
>>> d2 = x // 10
>>> print(d1, d2)
5 4
>>> 
>>> 
>>> 54 /10
5.4
>>> 54//10
5
>>> 54 % 10
4
>>> print(d1,d2)
5 4
>>> help print
SyntaxError: invalid syntax
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

>>> flush: whether to forcibly flush the stream.
SyntaxError: invalid syntax
>>> flush: whether to forcibly flush the stream.
KeyboardInterrupt
>>> 
>>> 
>>> print(d1, d2, sep='')
54
>>> print(d1, d2)
5 4
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
>>> x = 579
>>> reversed_x = x % 10 * 100 + x // 10 % 10 * 10 + x // 100 * 1
>>> reversed_x
975
>>> reversed_x // 5
195
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
>>> s *= 10
>>> s
30
>>> s /= 10
>>> s
3.0
>>> 5 / 2.5
2.0
>>> 5 + 1.0
6.0
>>> 6.0
6.0
>>> 
>>> int(5 + 8 / 4)
7
>>> 
>>> s = 15
>>> s // = 5
SyntaxError: invalid syntax
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
>>> 
============ RESTART: D:/199/8_7/22.10.07/შეტრიალებული რიცხვი.py ============
Enter an integer: 8593454848
Reversed number is 0
>>> 
============ RESTART: D:/199/8_7/22.10.07/შეტრიალებული რიცხვი.py ============
Enter an integer: 8593
Reversed number is 3958
>>> 
============ RESTART: D:/199/8_7/22.10.07/შეტრიალებული რიცხვი.py ============
Enter an integer: 1001002589
Reversed number is 9852001001
>>> 
