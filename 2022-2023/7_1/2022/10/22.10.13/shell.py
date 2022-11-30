Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
============= RESTART: D:\199\7_1\22.10.13\show_current_time.py =============
Current time is 8 : 52 : 25 GMT
>>> 
>>> 
>>> 
>>> x = 500
>>> x1 = x % 60
>>> x2 = x // 60
>>> x3 = x // 3600
>>> print(x3, x2, x1)
0 8 20
>>> print(x3, x2, x1, sep=':')
0:8:20
>>> 
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
>>> x = 137846
>>> x1 = x % 60
>>> x2 = x // 60 % 60
>>> x3 = x // 3600 % 24
>>> print(x3, x2, x1, sep=':')
14:17:26
>>> 14*3600 + 17*60 + 26
51446
>>> 38*3600 + 17*60 + 26
137846
>>> 
>>> 
>>> 
>>> import time
>>> time.time()
1665637873.706677
>>> 
>>> import time as t
>>> t.time()
1665637909.8315222
>>> 
>>> from time import time
>>> time()
1665637969.494441
>>> time()
1665637974.2686982
>>> int(time())
1665638017
>>> int(time())
1665638029
>>> int(time())
1665638031
>>> int(time())
1665638032
>>> int(time())
1665638115
>>> print(int(time()) // 3600 % 24,)
5
>>> print(int(time()) // 3600 % 24, int(time()) // 60 % 60, int(time()) % 60, sep=':')
5:17:9
>>> print(int(time()) // 3600 % 24 + 4, int(time()) // 60 % 60, int(time()) % 60, sep=':')
9:17:37
>>> 
