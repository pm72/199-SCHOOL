Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
not True
False
not False
True

not 5
False

not -1
False
not 0
True
not 0.0
True


5 > 3
True

not (5 > 3)
False

not 5 > 3
False

not 5 < 3
True



15 != 13 and not(2.78 <= -1.58)
True

15 != 13 and (2.78 <= -1.58)
False


x = 1900
x % 4 == 0 and x % 100 == 0
True

x = 1902
x % 4 == 0 and x % 100 == 0
False

====== RESTART: D:/199/8_6/2023/leap_year.py =====
Enter an year: 2016
2016 is leap

====== RESTART: D:/199/8_6/2023/leap_year.py =====
Enter an year: 1900
1900 isn't leap

====== RESTART: D:/199/8_6/2023/leap_year.py =====
Enter an year: 2004
2004 is leap

====== RESTART: D:/199/8_6/2023/leap_year.py =====
Enter an year: 2005
2005 isn't leap



x = 1900
if x:
    print("I have a money!")
else:
    print("I have a ZERO!")

    
I have a money!

x = 0
if x:
    print("I have a money!")
else:
    print("I have a ZERO!")

    
I have a ZERO!
>>> 
>>> 
>>> bool(1900)
True
>>> bool(x)
False
>>> 
>>> 
>>> 
>>> x = 1900
>>> if x < 2023:
...     print("YES")
... else:
...     print("NO")
... 
...     
YES
>>> x = 2023
>>> if x < 2023:
...     print("YES")
... else:
...     print("NO")
... 
...     
NO
