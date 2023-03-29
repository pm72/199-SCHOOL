Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#  str, int, float
# bool

not False
True
not True
False

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



5 > 3 and not (7.21 <= -5.9)
True


x = 1900
x % 4 == 0 and x % 100 == 0
True

===== RESTART: D:/199/8_1/2023/leap_year.py =====
Enter an year: 2012
2012 is leap

===== RESTART: D:/199/8_1/2023/leap_year.py =====
Enter an year: 2010
2010 isn't leap

===== RESTART: D:/199/8_1/2023/leap_year.py =====
Enter an year: 1900
1900 isn't leap

===== RESTART: D:/199/8_1/2023/leap_year.py =====
Enter an year: 2014
2014 isn't leap



x = 1900
if x:
    print("I have money!")
else:
    print("I have ZERo!")

    
I have money!

bool(1900)
True
>>> 

>>> x = 0
>>> if x:
...     print("I have money!")
... else:
...     print("I have ZERo!")
... 
...     
I have ZERo!
>>> 
>>> 
>>> if x > 2000:
...     print("YES")
... else:
...     print("NO")
... 
...     
NO
>>> 
>>> x = 2023
>>> if x > 2000:
...     print("YES")
... else:
...     print("NO")
... 
...     
YES
