Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
============ RESTART: D:\199\7_3\22.9.28\copute_are_of_circle.py ============
The area of the circle with radius 20.58 is 1330.5777188759998
The length of the circle with radius 20.58 is 129.3078444

============ RESTART: D:\199\7_3\22.9.28\copute_are_of_circle.py ============
The area of the circle with radius 20.58 is 1330.5777188759998
The length of the circle with radius 20.58 is 129.3078444

>>> Pi
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    Pi
NameError: name 'Pi' is not defined
>>> PI
15
>>> 
============ RESTART: D:\199\7_3\22.9.28\copute_are_of_circle.py ============
The area of the circle with radius 20.58 is 1330.5777188759998
The length of the circle with radius 20.58 is 129.3078444

>>> pi
15
>>> PI
3.14159
>>> 
============ RESTART: D:\199\7_3\22.9.28\copute_are_of_circle.py ============
The area of the circle with radius 20.58 is 1330.5777188759998
The length of the circle with radius 20.58 is 129.3078444

============ RESTART: D:\199\7_3\22.9.28\copute_are_of_circle.py ============
The area of the circle with radius 20.58 is 1331
The length of the circle with radius 20.58 is 129.3078444

============ RESTART: D:\199\7_3\22.9.28\copute_are_of_circle.py ============
The area of the circle with radius 20.58 is 1330.58
The length of the circle with radius 20.58 is 129.3078444

============ RESTART: D:\199\7_3\22.9.28\copute_are_of_circle.py ============
The area of the circle with radius 20.58 is 1330.58
The length of the circle with radius 20.58 is 129.31

============ RESTART: D:\199\7_3\22.9.28\copute_are_of_circle.py ============
The area of the circle with radius 20.58 is 1330.578
The length of the circle with radius 20.58 is 129.31

============ RESTART: D:\199\7_3\22.9.28\copute_are_of_circle.py ============
The area of the circle with radius 20.58 is 1330.6
The length of the circle with radius 20.58 is 129.31

============ RESTART: D:\199\7_3\22.9.28\copute_are_of_circle.py ============31
The area of the circle with radius 20.58 is 1330.58
The length of the circle with radius 20.58 is 129.31

>>> 
============ RESTART: D:\199\7_3\22.9.28\copute_are_of_circle.py ============

Traceback (most recent call last):
  File "D:\199\7_3\22.9.28\copute_are_of_circle.py", line 8, in <module>
    area = round(PI * radius ** 2, 2)
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
>>> 
============ RESTART: D:\199\7_3\22.9.28\copute_are_of_circle.py ============
Enter value of circle radius: 17.58
Traceback (most recent call last):
  File "D:\199\7_3\22.9.28\copute_are_of_circle.py", line 8, in <module>
    area = round(PI * radius ** 2, 2)
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
>>> radius
'17.58'
>>> type(radius)
<class 'str'>
>>> int(radius)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    int(radius)
ValueError: invalid literal for int() with base 10: '17.58'
>>> int('5')
5
>>> float('2.89')
2.89
>>> int('17.58')
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    int('17.58')
ValueError: invalid literal for int() with base 10: '17.58'
>>> int(17.96)
17
>>> float(1)
1.0
>>> eval('1.56')
1.56
>>> eval('25')
25
>>> 
============ RESTART: D:\199\7_3\22.9.28\copute_are_of_circle.py ============
Enter value of circle radius: 17.58
The area of the circle with radius 17.58 is 970.93
The length of the circle with radius 17.58 is 110.46
