Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
================= RESTART: D:\199\7_3\22.10.10\sales_tax.py =================
Enter purchase amount: 255.69
Sales tax is 25.57
Total pay is 281.26
>>> 
================= RESTART: D:\199\7_3\22.10.10\sales_tax.py =================
Enter purchase amount: 157.20
Sales tax is 15.72
Total pay is 172.92
>>> 
>>> 
>>> x = 500
>>> sec = x % 60
>>> x
500
>>> sec
20
>>> min = x // 60
>>> 
>>> print(min, sec)
8 20
>>> print(min, sec, sep=':')
8:20
>>> 
>>> hr = x // 3600
>>> print(hr, min, sec, sep=':')
0:8:20
>>> 
>>> 
>>> x = 5000
>>> sec = x % 60
>>> min = x // 60 % 60
>>> hr = x // 3600
>>> print(hr, min, sec, sep=':')
1:23:20
>>> 1*3600 + 23 * 60 + 20
5000
>>> 
>>> x = 10000
>>> sec = x % 60
>>> min = x // 60 % 60
>>> hr = x // 3600
>>> print(hr, min, sec, sep=':')
2:46:40
>>> 
>>> 
>>> x = 38000
>>> sec = x % 60
>>> min = x // 60 % 60
>>> hr = x // 3600
>>> print(hr, min, sec, sep=':')
10:33:20
>>> 
>>> x = 380000
>>> sec = x % 60
>>> min = x // 60 % 60
>>> hr = x // 3600
>>>  print(hr, min, sec, sep=':')
 
SyntaxError: unexpected indent
>>> print(hr, min, sec, sep=':')
105:33:20
>>> hr = x // 3600 % 24
>>> print(hr, min, sec, sep=':')
9:33:20
>>> 
>>> 
>>> import time as t
>>> t.time()
1665397074.721799
>>> t.time()
1665397078.5783982
>>> t.time()
1665397080.2430665
>>> t.time()
1665397081.578365
>>> int(t.time())
1665397177
>>> int(t.time())
1665397182
>>> int(t.time())
1665397183
>>> 
============= RESTART: D:\199\7_3\22.10.10\show_current_time.py =============
Current time is 10 : 19 : 49 GMT
>>> 
============= RESTART: D:\199\7_3\22.10.10\show_current_time.py =============
Current time is 10 : 22 : 23 GMT
>>> 
============= RESTART: D:\199\7_3\22.10.10\show_current_time.py =============
Current time is 10 : 28 : 17 GMT
>>> 
============= RESTART: D:\199\7_3\22.10.10\show_current_time.py =============
Current time is 14 : 28 : 51 GMT
>>> 
============= RESTART: D:\199\7_3\22.10.10\show_current_time.py =============
Current time is 14 : 30 : 18 GMT
>>> 
