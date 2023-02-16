Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
not (2 > 3)
True

not 5
False

===== RESTART: D:/199/7_7/2023/test_boolean_operators.py ====
Enter an integer: 18
18 divide by 2 and 3

===== RESTART: D:/199/7_7/2023/test_boolean_operators.py ====
Enter an integer: 21

===== RESTART: D:/199/7_7/2023/test_boolean_operators.py ====
Enter an integer: 15
15 divide by 2 or 3

===== RESTART: D:/199/7_7/2023/test_boolean_operators.py ====
Enter an integer: 11

===== RESTART: D:/199/7_7/2023/test_boolean_operators.py ====
Enter an integer: 14
14 divide by 2 or 3 but not both


>>> 
>>> not (x > 0) and (x > 0)
False
>>> 
>>> not (x > 0) and (x < 0)
False
>>> 
>>> not ((x > 0) and (x < 0))
True
>>> 
>>> 
>>> num = 97
>>> print(1 <= num <= 100)
True
>>> 
>>> 
>>> print(1 <= num <= 100 or num < 0)
True
>>> 
>>> num = 101
>>> print(1 <= num <= 100 or num < 0)
False
>>> 
>>> num = -7
>>> print(1 <= num <= 100 or num < 0)
True
