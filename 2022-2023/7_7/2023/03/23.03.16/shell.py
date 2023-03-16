Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x, y, z = eval(input("Enter three numbers: "))
Enter three numbers: 2, 3, 6.
>>> x
2
>>> y
3
>>> z
6.0
>>> 
>>> 
>>> x, y, z = 2, 3, 6
>>> 
>>> 
>>> x, y = 2, 3, 6
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    x, y = 2, 3, 6
ValueError: too many values to unpack (expected 2)
>>> 
>>> x, y, z = 2, 3
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    x, y, z = 2, 3
ValueError: not enough values to unpack (expected 3, got 2)

x, y, z = 2, 3, None
z
type(z)
<class 'NoneType'>

z + 1
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    z + 1
TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'

int(z)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    int(z)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'NoneType'


5 < 7.2 and not(2.54 < -1.89)
True


x = 1900
x % 4 == 0 and x % 100 == 0
True

x = 1902
x % 4 == 0 and x % 100 == 0
False



===================== RESTART: D:/199/7_7/2023/leap_year.py ====================
Enter an year: 1958
1958 isn't leap

=========== RESTART: D:/199/7_7/2023/leap_year.py ==========
Enter an year: 2016
2016 is leap



x = 1900
if x:
    print("YES, I have a money")
else:
    print("NO, I have ZERO")

    
YES, I have a money


x = 0
if x:
    print("YES, I have a money")
else:
    print("NO, I have ZERO")

    
NO, I have ZERO

bool(1900)
True
bool(0)
False

=========== RESTART: D:/199/7_7/2023/leap_year.py ==========
Enter an year: 1900
1900 isn't leap
1900 isn't leap

=========== RESTART: D:/199/7_7/2023/leap_year.py ==========
Enter an year: 2012
2012 is leap
2012 is leap
