Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
not True
False
not Fase
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    not Fase
NameError: name 'Fase' is not defined. Did you mean: 'False'?
not False
True


not 5
False
not 0
True
not None
True
not ''
True


5 > 3
True
not (5 > 3)
False
not 5 > 3
False

not 5 < 3
True


int(not 5)
0
int(not 0)
1



5 > 2.3 and not(2.89 < -1.89)
True


x = 1900
x % 4 == 0 and x % 100 == 0
True


>>> x = 1902
>>> x % 4 == 0 and x % 100 == 0
False
>>> 
>>> 
>>> 
>>> 
====== RESTART: D:/199/8_3/2023/leap_year.py ======
Enter year: 1900
1900 isn't leap year
>>> 
====== RESTART: D:/199/8_3/2023/leap_year.py ======
Enter year: 
====== RESTART: D:/199/8_3/2023/leap_year.py ======
Enter year: 1904
1904 is leap year
>>> 
====== RESTART: D:/199/8_3/2023/leap_year.py ======
Enter year: 1900
1900 isn't leap year
1900 isn't leap year
>>> 
====== RESTART: D:/199/8_3/2023/leap_year.py ======
Enter year: 1904
1904 is leap year
1904 is leap year
