Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import time
>>> time.time()
1665048100.5278912
>>> time.time()
1665048111.6702976
>>> time.time()
1665048114.3297064
>>> 
>>> 
>>> sec = 1665048114
>>> sec % 60
54
>>> minutes = sec // 60 % 60
>>> minutes
21
>>> hours = sec // 60
>>> hours
27750801
>>> hours % 24
9
>>> current_hours = hourse % 24
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    current_hours = hourse % 24
NameError: name 'hourse' is not defined
>>> current_hours = hours % 24
>>> current_hours
9
>>> print(current_hours, minutes, sec % 60, sep=':')
9:21:54
>>> print(current_hours + 4, minutes, sec % 60, sep=':')
13:21:54
>>> 
============= RESTART: D:\199\7_2\22.10.06\show_current_time.py =============
Current time is 9 : 35 : 52 GMT
>>> 
============= RESTART: D:\199\7_2\22.10.06\show_current_time.py =============
Current time is 9 : 36 : 2 GMT
>>> 
