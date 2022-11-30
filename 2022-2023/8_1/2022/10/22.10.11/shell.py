Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
============= RESTART: D:\199\8_1\22.10.11\show_current_time.py =============
Current time is 11 : 35 : 19 GMT
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
>>> 0 * 3600 + 8 * 60 + 20
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
>>> x = 117000
>>> x1 = x % 60
>>> x2 = x // 60 % 60
>>> x3 = x // 3600 % 24
>>> print(x3, x2, x1, sep=':')
8:30:0
>>> 83*3600 + 30*60
300600
>>> 23 * 3600 + 30*60
84600
>>> 32 * 3600 + 30 * 90
117900
>>> 32 * 3600 + 30 * 60
117000
>>> 
>>> 
>>> 
>>> import time
>>> time.time()
1665474529.335513
>>> 
>>> import time as t
>>> t.time()
1665474566.762048
>>> 
>>> 
>>> from time import time
>>> time()
1665474632.8008833
>>> time()
1665474650.440397
>>> time()
1665474652.4336088
>>> time()
1665474654.6647844
>>> int(time())
1665474794
>>> int(time())
1665474797
>>> int(time())
1665474798
>>> int(time())
1665474800
>>> print(int(time()) // 3600 % 24, int(time()) // 60 % 60, int(time() % 60), sep=':')
7:55:38
>>> print(int(time()) // 3600 % 24, int(time()) // 60 % 60, int(time() % 60), sep=':')
7:55:43
>>> print(int(time()) // 3600 % 24, int(time()) // 60 % 60, int(time() % 60), sep=':')
7:55:45
>>> print(int(time()) // 3600 % 24 + 4, int(time()) // 60 % 60, int(time() % 60), sep=':')
11:56:17
>>> print((int(time()) // 3600 % 24 + 4) % 24, int(time()) // 60 % 60, int(time() % 60), sep=':')
11:58:55
>>> print((int(time()) // 3600 % 24 + 4) % 24, int(time()) // 60 % 60, int(time() % 60), sep=':')
11:59:1
>>> 
============= RESTART: D:\199\8_1\22.10.11\show_current_time.py =============
Current time is 12 : 2 : 21 GMT
>>> 
============= RESTART: D:\199\8_1\22.10.11\show_current_time.py =============
Current time is 12 : 2 : 39 GMT+4
>>> print(int(time()) // 3600 % 24 + 4, int(time()) // 60 % 60, int(time() % 60), sep=':')
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    print(int(time()) // 3600 % 24 + 4, int(time()) // 60 % 60, int(time() % 60), sep=':')
TypeError: 'module' object is not callable
>>> from time import time
>>> print(int(time()) // 3600 % 24 + 4, int(time()) // 60 % 60, int(time() % 60), sep=':')
12:3:7
>>> 
============= RESTART: D:\199\8_1\22.10.11\show_current_time.py =============
Current time is 12 : 3 : 11 GMT+4
>>> 
