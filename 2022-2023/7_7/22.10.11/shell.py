Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> x = 500
>>> x1 = x % 60
>>> x2 = x // 60
>>> x3 = x // 3600
>>> print(x3, x2, x1)
0 8 20
>>> print(x3,x2,x1,sep=':')
0:8:20
>>> 
>>> 
>>> x = 5000
>>> x1 = x % 60
>>>  x2 = x // 60
 
SyntaxError: unexpected indent
>>> x2 = x // 60 % 60
>>> x2
23
>>> x3 = x // 3600 % 24
>>> print(x3, x2, x1, sep=':')
1:23:20
>>> 
>>> 
>>> from time import time
>>> time()
1665464896.9390852
>>> current_seconds = int(time())
>>> current_seconds
1665464981
>>> current_seconds
1665464981
>>> current_seconds
1665464981
>>> seconds = current_seconds % 60
>>> seconds
41
>>> total_minutes = current_seconds // 60
>>> total_minutes
27757749
>>> minutes = total_minutes % 60
>>> minutes
9
>>> total_hours = total_minutes // 60
>>> total_hours
462629
>>> current_hours = total_hours % 24
>>> current_hours
5
>>> print(current_hours, minutes, seconds, sep=':')
5:9:41
>>> print((current_hours + 4) % 24, minutes, seconds, sep=':')
9:9:41
>>> 
