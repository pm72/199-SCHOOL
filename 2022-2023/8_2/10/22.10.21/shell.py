Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> x = 500
>>> x1 = x % 60
>>> x2 = x // 60
>>> x3 = x // 3600
>>> print(x3, x2, x1)
0 8 20
>>> print(x3, x2, x1, sep=':')
0:8:20
>>> print(x3, x2, x1)
0 8 20
>>> 
>>> x = 5000
>>> x1 = x % 60
>>> x2 = x // 60 % 60
>>> x3 = x // 3600
>>> print(x3, x2, x1, sep=':')
1:23:20
>>> 1*3600 + 23*60 + 20
5000
>>> 
>>> 
>>> x = 137852
>>> x1 = x % 60
>>> x2 = x // 60 % 60
>>> x3 = x // 3600 % 24
>>> print(x3, x2, x1, sep=':')
14:17:32
>>> 38*3600 + 17*60 + 32
137852
>>> 
>>> 
>>> 
>>> import time
>>> time.time()
1666329262.3725636
>>> 
>>> 
>>> from time import time
>>> 
