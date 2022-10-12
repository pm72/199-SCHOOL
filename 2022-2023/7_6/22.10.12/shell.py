Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
============= RESTART: D:\199\7_6\22.10.12\show_current_time.py =============
Current time is 13 : 20 : 7 GMT
>>> 
============= RESTART: D:\199\7_6\22.10.12\show_current_time.py =============
Current time is 13 : 20 : 28 GMT+4
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
>>> 0 * 3600 + 8*60 + 20
500
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
>>> x = 156328
>>> x1 = x % 60
>>> 2 = x // 60 % 60
SyntaxError: can't assign to literal
>>> x2 = x // 60 % 60
>>> x3 = x // 3600 % 24
>>> print(x3, x2, x1, sep=':')
19:25:28
>>> 19*3600 + 25*60 + 28
69928
>>> 43*3600 + 25*60 + 28
156328
>>> 
>>> 
>>> 
>>> import time
>>> time.time()
1665567449.7363808
>>> 
>>> 
>>> from time import time
>>> time()
1665567605.7589068
>>> time()
1665567623.2333467
>>> time()
1665567625.505752
>>> int(time())
1665567659
>>> int(time())
1665567662
>>> int(time())
1665567664
>>> int(time())
1665567752
>>> print(int(time()) // 3600 % 24, int(time()) // 60 % 60, int(time()) % 60, sep=':')
9:45:4
>>> print(int(time()) // 3600 % 24 + 4, int(time()) // 60 % 60, int(time()) % 60, sep=':')
13:46:40
>>> print((int(time()) // 3600 % 24 + 4) % 24, int(time()) // 60 % 60, int(time()) % 60, sep=':')
13:47:50
>>> 
