Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
============= RESTART: D:\199\7_5\22.10.12\show_current_time.py =============
Current time is 10 : 30 : 51 GMT
>>> 
============= RESTART: D:\199\7_5\22.10.12\show_current_time.py =============
Current time is 10 : 31 : 10 GMT
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

>>> x = 178239
>>> x1 = x % 60
>>> x2 = x // 60 % 60
>>> x3 = x // 3600 % 24
>>> print(x3, x2, x1, sep=':')
1:30:39
>>> 49*3600 + 30*60 + 39
178239
>>> 
>>> 
>>> 
>>> import time
>>> time.time()
1665557253.3666306
>>> time.time()
1665557264.803345
>>> time.time()
1665557269.2092738
>>> time.time()
1665557271.0216415
>>> time.time()
1665557345.6880643
>>> time.time()
1665557356.2810035
>>> int(time.time())
1665557393
>>> int(time.time())
1665557398
>>> int(time.time())
1665557401
>>> 
>>> 
>>> from time import time
>>> int(time)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    int(time)
TypeError: int() argument must be a string, a bytes-like object or a number, not 'builtin_function_or_method'
>>> int(time())
1665557443
>>> int(time())
1665557445
>>> 
>>> 
>>> print(int(time()) // 3600 % 24, int(time()) // 60 % 60, int(time()) % 60, sep=':')
6:52:4
>>> print(int(time()) // 3600 % 24  + 4, int(time()) // 60 % 60, int(time()) % 60, sep=':')
10:52:46
>>> print((int(time()) // 3600 % 24  + 4) % 24, int(time()) // 60 % 60, int(time()) % 60, sep=':')
10:53:49
>>> print((int(time()) // 3600 % 24  + 4) % 24, int(time()) // 60 % 60, int(time()) % 60, sep=':')
10:54:7
>>> print((int(time()) // 3600 % 24  + 4) % 24, int(time()) // 60 % 60, int(time()) % 60, sep=':')
10:54:10
>>> 
============= RESTART: D:\199\7_5\22.10.12\show_current_time.py =============
Current time is 10 : 56 : 33 GMT+4
>>> 
