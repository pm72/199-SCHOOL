Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
year = 1900

print((year % 4 == 0 and year % 100 != 0) or year % 400 == 0)
False


year = 2000
print((year % 4 == 0 and year % 100 != 0) or year % 400 == 0)
True

year = 2004
print((year % 4 == 0 and year % 100 != 0) or year % 400 == 0)
True


year = 1996
print((year % 4 == 0 and year % 100 != 0) or year % 400 == 0)
True


============= RESTART: D:/199/7_5/2023/leep_year.py =============
Enter an year: 2002
Traceback (most recent call last):
  File "D:/199/7_5/2023/leep_year.py", line 6, in <module>
    if leep_year() == True:
TypeError: 'bool' object is not callable

============= RESTART: D:/199/7_5/2023/leep_year.py =============
Enter an year: 2002
2002 is not leep

============= RESTART: D:/199/7_5/2023/leep_year.py =============
Enter an year: 2008
2008 is leep

============= RESTART: D:/199/7_5/2023/leep_year.py =============
Enter an year: 1700
1700 is not leep

============= RESTART: D:/199/7_5/2023/leep_year.py =============
Enter an year: 2000
2000 is leep

============== RESTART: D:/199/7_5/2023/lottery.py ==============
79

============== RESTART: D:/199/7_5/2023/lottery.py ==============
10

============== RESTART: D:/199/7_5/2023/lottery.py ==============
19

============== RESTART: D:/199/7_5/2023/lottery.py ==============
82

======= RESTART: D:/199/7_5/2023/lottery.py ======
35
Enter your lottery pick (two digits): 45
Match one digit: you win $1,000

======= RESTART: D:/199/7_5/2023/lottery.py ======
69
Enter your lottery pick (two digits): 45
The lottery number is 69
Sorry, no match
>>> 
======= RESTART: D:/199/7_5/2023/lottery.py ======
Enter your lottery pick (two digits): 15
The lottery number is 83
Sorry, no match
>>> 
======= RESTART: D:/199/7_5/2023/lottery.py ======
Enter your lottery pick (two digits): 56
The lottery number is 57
Match one digit: you win $1,000
>>> 
>>> 
>>> 
>>> 
>>> x = 56.
>>> if x > 0:
...     y = 1
... else:
...     y = -1
... 
...     
>>> y
1
>>> 
>>> y = 1 if x > 0 else -1
>>> y
1
