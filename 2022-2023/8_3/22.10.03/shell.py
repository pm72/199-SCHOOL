Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> x = 20
>>> y = 15
>>> 
>>> x = x + y
>>> y = x - y
>>> x = y - x
>>> 
>>> x, y
(-15, 20)
>>> 
>>> 
>>> x = 20
>>> y = 15
>>> 
>>> temp = x
>>> x = y
>>> y = temp
>>> 
>>> x, y
(15, 20)
>>> 
>>> 
>>> x = 20
>>> y = 15
>>> 
>>> x,y
(20, 15)
>>> 
>>> x, y = y, x
>>> 
>>> x, y
(15, 20)
>>> 
>>> 
>>> x = 20
>>> type(x)
<class 'int'>
>>> type(20)
<class 'int'>
>>> id(x)
1927600224
>>> id(20)
1927600224
>>> 
>>> from sys import getsizeof
>>> getsizeof(x)
14
>>> getsizeof(20)
14
>>> getsizeof(2**25)
16
>>> 

>>> x, y = 15, 25,
>>> x, y = 15, 25, 33
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    x, y = 15, 25, 33
ValueError: too many values to unpack (expected 2)
>>> 
>>> 
>>> x, y, z = 15, 55
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    x, y, z = 15, 55
ValueError: not enough values to unpack (expected 3, got 2)
>>> 
>>> 
>>> 
>>> 8/4
2.0
>>> 
>>> 8 // 5
1
>>> 9 // 5
1
>>> 8 // 4
2
>>> 
>>> 8 % 5
3
>>> 10 % 5
0
>>> 5 % 8
5
>>> 5/8
0.625
>>> 5//8
0
>>> 
>>> 
>>> x = 45
>>> x % 10 + x // 10
9
>>> 
>>> x
45
>>> 
>>> print(x % 10, x // 10)
5 4
>>> print(x % 10, x // 10, sep='')
54
>>> 
>>> y = x % 10 * 10 + x // 10
>>> y
54
>>> y * 2
108
>>> 
>>> 
>>> x = 18745
>>> 
================== RESTART: D:/199/8_3/22.10.03/numbers.py ==================
Enter an integer number: 584
Traceback (most recent call last):
  File "D:/199/8_3/22.10.03/numbers.py", line 5, in <module>
    revers += (x % 10)
NameError: name 'revers' is not defined
>>> 
================== RESTART: D:/199/8_3/22.10.03/numbers.py ==================
Enter an integer number: 254
11
>>> 
================== RESTART: D:/199/8_3/22.10.03/numbers.py ==================
Enter an integer number: 12
30
>>> 
================== RESTART: D:/199/8_3/22.10.03/numbers.py ==================
Enter an integer number: 12
21
>>> 
================== RESTART: D:/199/8_3/22.10.03/numbers.py ==================
Enter an integer number: 589741
147985
>>> _ * 10
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    _ * 10
NameError: name '_' is not defined
>>> reverse * 10
1479850
>>> 
