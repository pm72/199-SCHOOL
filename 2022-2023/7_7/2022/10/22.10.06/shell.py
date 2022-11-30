Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> numb = 5984
>>> sec = numb % 60
>>> minutes = numb // 60 % 60
>>> hours = numb // 3600 % 24
>>> print(hours, minutes, sec, sep=':')
1:39:44
>>> 
>>> 
>>> 
>>> import time as t
>>> t.time()
1665050897.6676326
>>> t.time()
1665050903.7612906
>>> t.time()
1665050905.498305
>>> int(t.time())
1665051016
>>> 
============= RESTART: D:\199\7_7\22.10.06\show_current_time.py =============
Current time is 10 : 14 : 43 GMT
>>> 
============= RESTART: D:\199\7_7\22.10.06\show_current_time.py =============
Current time is:10:15:15:GMT
>>> 
============= RESTART: D:\199\7_7\22.10.06\show_current_time.py =============
Current time is 10:17:53 GMT
>>> 
============= RESTART: D:\199\7_7\22.10.06\show_current_time.py =============
Current time is 14:18:4 GMT
>>> 
============= RESTART: D:\199\7_7\22.10.06\show_current_time.py =============
Current time is 14:18:14 GMT
>>> 
============= RESTART: D:\199\7_7\22.10.06\show_current_time.py =============
Current time is 14:18:16 GMT
>>> 
============= RESTART: D:\199\7_7\22.10.06\show_current_time.py =============
Current time is 14:18:18 GMT
>>> 
