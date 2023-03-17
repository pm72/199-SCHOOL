Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
not True
False
not False
True
not 5
False
not -1
False
not 0
True
not 0.0
True
not None
True
not ''
True



5 > 3
True
not (5 > 3)
False
not 5 > 3
False
not 5 < 3
True



5 > 3 and not(2.78 <= -1.5)
True


x = 1900
x % 4 == 0 and x % 100 == 0
True

x = 1902
x % 4 == 0 and x % 100 == 0
False


'a' <= 'd' and 'Z' > '0'
True
>>> 
>>> x = 'Paata'
>>> y = 'paata'
>>> 
>>> x == y
False
>>> x > y
False
>>> x - y
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    x - y
TypeError: unsupported operand type(s) for -: 'str' and 'str'
>>> 
>>> int('p') - int('P')
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    int('p') - int('P')
ValueError: invalid literal for int() with base 10: 'p'
>>> ord('p')
112
>>> ord('p') - ord('P')
32
>>> 
>>> 
>>> 
