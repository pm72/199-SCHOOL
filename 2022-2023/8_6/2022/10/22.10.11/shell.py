Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
================= RESTART: D:\199\8_6\22.10.11\sales_tax.py =================
Enter purchase amount: 155.55
Sales tax is 9.33
Total pay is 164.88
>>> 
================= RESTART: D:\199\8_6\22.10.11\sales_tax.py =================
Enter purchase amount: 258
Sales tax is 15.48
Total pay is 273.48
>>> 
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
>>> .
SyntaxError: invalid syntax
>>> 
>>> 
>>> x = 5000
>>> x1 = x % 60
>>> x2 = x // 60 % 60
>>> x3 = x // 3600
>>> print(x3, x2, x1, sep=':')
1:23:20
>>> 1 * 3600 + 23 * 60 + 20
5000
>>> 
>>> 
>>> x = 80000
>>> x1 = x % 60
>>> x2 = x // 60 % 60
>>> x3 = x // 3600
>>> 
>>> 
>>> x = 120000
>>> x1 = x % 60
>>> x2 = x // 60 % 60
>>> x3 = x // 3600 % 24
>>> print(x3, x2, x1, sep=':')
9:20:0
>>> 9*3600 + 20 * 60
33600
>>> 9*3600*24 + 20 * 60
778800
>>> 33*3600 + 20*60
120000
>>> 
>>> 
>>> 
>>> 
>>> from  time import time
>>> time()
1665467606.3776042
>>> int(time())
1665467650
>>> int(time())
1665467655
>>> int(time())
1665467656
>>> x1 = int(time()) % 60
>>> x1
55
>>> x2 = int(time()) // 60 % 60
>>> x2
55
>>> x1
55
>>> x3 = int(time()) // 3600 % 24
>>> print(x3, x2, x1, sep=':')
5:55:55
>>> print(int(time()) % 60, int(time()) // 60 % 60, int(time()) // 3600 % 24, sep=':')
27:57:5
>>> print(int(time()) % 60, int(time()) // 60 % 60, int(time()) // 3600 % 24, sep=':')
59:57:5
>>> print(int(time()) // 3600 % 24, int(time()) // 60 % 60, int(time()) % 60, sep=':')
5:58:42
>>> print(int(time()) // 3600 % 24, int(time()) // 60 % 60, int(time()) % 60, sep=':')
5:58:47
>>> print(int(time()) // 3600 % 24 + 4, int(time()) // 60 % 60, int(time()) % 60, sep=':')
9:59:16
>>> print((int(time()) // 3600 % 24 + 4) % 24, int(time()) // 60 % 60, int(time()) % 60, sep=':')
10:0:18
>>> 
