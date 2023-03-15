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
not -1.258
False



5 > 7 and 5 != 5
False

(5 > 7) and (5 == 5)
False

(5 < 7) and (5 == 5)
True
5 < 7 and 5 == 5
True

5 < (7 and 5) == 5
False

5 < (7 and 5) == 0
False

5 < (7 and 5)
False

5 < (7 and 5) == bool(0)
False

bool(5 < (7 and 5)) == bool(0)
True

bool(1)
True
int(true)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    int(true)
NameError: name 'true' is not defined. Did you mean: 'True'?
int(True)
1
float(False)
0.0

str(True)
'True'


====== RESTART: D:/199/7_3/2023/leap_year.py =====
Enter an year: 2012
2012 is leap

====== RESTART: D:/199/7_3/2023/leap_year.py =====
Enter an year: 1900
1900 is't leap

====== RESTART: D:/199/7_3/2023/leap_year.py =====
Enter an year: 1900
1900 is't leap
1900 is't leap



value = 1999
if value:
    print("YES, I have any value")
else:
    print("Not, U have ZERO")

...     
YES, I have any value
>>> 
>>> bool(1999)
True
>>> 
>>> value = 0
>>> if value:
...     print("YES, I have any value")
... else:
...     print("Not, U have ZERO")
... 
...     
Not, U have ZERO
>>> 
>>> 
>>> if va
SyntaxError: expected ':'
>>> 
>>> 
>>> 
>>> IF value < 2000: print("YES")
SyntaxError: invalid syntax
>>> 
>>> if value < 2000: print("YES")
... 
YES
