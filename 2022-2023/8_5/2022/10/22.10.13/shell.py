Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
============= RESTART: D:\199\8_5\22.10.13\show_current_time.py =============
Current time is 10 : 25 : 19 GMT
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
>>> 0*3600 + 8*60 + 20
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
>>> 1*3600 + 23*60 + 20
5000
>>> 
>>> 
>>> x = 137563
>>> x1 = x % 60
>>> x2 = x // 60 % 60
>>> x3 = x // 3600 % 24
>>> print(x3, x2, x1, sep=':')
14:12:43
>>> 38*3600 + 12*60 + 43
137563
>>> 
>>> 
>>> 
>>> import time
>>> time.time()
1665643109.15506
>>> time.time()
1665643117.5815005
>>> time.time()
1665643119.9044063
>>> time()
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    time()
TypeError: 'module' object is not callable
>>> time.time()
1665643267.1940248
>>> 
>>> from time import time
>>> time()
1665643320.521606
>>> 
>>> 
>>> int(time())
1665643347
>>> int(time())
1665643351
>>> int(time())
1665643353
>>> 
>>> print(int(time()) // 3600 % 24, int(time()) // 60 % 60, int(time()) % 60, sep=':')
6:45:2
>>> print(int(time()) // 3600 % 24, int(time()) // 60 % 60, int(time()) % 60, sep=':')
6:45:16
>>> print(int(time()) // 3600 % 24 + 4, int(time()) // 60 % 60, int(time()) % 60, sep=':')
10:46:0
>>> print((int(time()) // 3600 % 24 + 4) % 24, int(time()) // 60 % 60, int(time()) % 60, sep=':')
10:48:49
>>> 
============= RESTART: D:\199\8_5\22.10.13\show_current_time.py =============
Current time is 10 : 52 : 31 GMT+4
>>> 
============= RESTART: D:\199\8_5\22.10.13\show_current_time.py =============
Current time is 3 : 52 : 48 GMT+4
>>> 
============= RESTART: D:\199\8_5\22.10.13\show_current_time.py =============
Current time is 6 : 53 : 0 GMT+4
>>> 
