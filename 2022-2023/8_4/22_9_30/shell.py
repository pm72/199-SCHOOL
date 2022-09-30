Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
================ RESTART: D:\199\8_4\22.9.30\წრის ფართობი.py ================
Enter the radius: 25
>>> 
>>> 
>>> from math import pi
>>> pi
3.141592653589793
>>> 3.45 ** 2 * pi
37.392806559352515
>>> 3.45 ** 2 * 3.14
37.373850000000004
>>> 
================ RESTART: D:\199\8_4\22.9.30\წრის ფართობი.py ================
Enter the radius: 25
Traceback (most recent call last):
  File "D:\199\8_4\22.9.30\წრის ფართობი.py", line 7, in <module>
    area = PI * radius ** 2
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
>>> radius
'25'
>>> type(radius)
<class 'str'>
>>> 
>>> 
>>> int('25')
25
>>> float('2.58')
2.58
>>> 
>>> 
