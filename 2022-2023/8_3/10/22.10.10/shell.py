Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> x = 500
>>> seconds = x % 60
>>> minutes = x // 60
>>> hours = x // 3600
>>> print(hours, minutes, seconds, sep=':')
0:8:20
>>> x = 5000
>>> seconds = x % 60
>>> minutes = x // 60
>>> 
>>> hours = x // 3600
>>> print(hours, minutes, seconds, sep=':')
1:83:20
>>> 83*60
4980
>>> minutes = (x - x % 60) % 60
>>> minutes
0
>>> minutes = (x - x % 60) // 60 % 60
>>> minutes
23
>>> print(hours, minutes, seconds, sep=':')
1:23:20
>>> 3600 + 23*60 + 20
5000
>>> 5000
5000

>>> 
>>> 
>>> x = 10000
>>> seconds = x % 60
>>> minutes = (x - x % 60) % 60
>>> hours = x // 3600
>>> print(hours, minutes, seconds, sep=':')
2:0:40
>>> minutes = (x - x % 60) // 60 % 60
>>> print(hours, minutes, seconds, sep=':')
2:46:40
>>> 2*3600+46*60+40
10000
>>> 
>>> 
>>> 
>>> import time as t
>>> t.tome()
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    t.tome()
AttributeError: module 'time' has no attribute 'tome'
>>> t.time()
1665394180.5795398
>>> t.time()
1665394198.3354537
>>> t.time()
1665394201.3876352
>>> t.time()
1665394203.8521242
>>> int(t.time())
1665394222
>>> int(t.time())
1665394225
>>> 
>>> 
>>> t.time() % 60
5.699057340621948
>>> int(t.time()) % 60
30
>>> int(t.time()) % 60
33
>>> int(t.time()) // 60
27756573
>>> int(t.time()) // 60 % 60
33
>>> totalSeconds // 60 // 60
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    totalSeconds // 60 // 60
NameError: name 'totalSeconds' is not defined
>>> 
