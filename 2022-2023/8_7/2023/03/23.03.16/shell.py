Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    a
NameError: name 'a' is not defined
a = None
a
type(a)
<class 'NoneType'>
a + 1
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    a + 1
TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'

print(print())

None


def foo():
    print("Hello")

    
foo()
Hello

print(foo)
<function foo at 0x000001F85FE5F760>

print(foo())
Hello
None


not True
False
not False
True
not 5
False
not -5
False
not 0
True


5 > 3
True
not (5 > 3)
False

not 5 > 3
False

not 5 < 3
True


5 > 3 and 2.17 < -1.58
False

5 > 3 and not (2.17 < -1.58)
True

x = 1900
x % 4 == 0 and x % 100 == 0
True

x = 1902
x % 4 == 0 and x % 100 == 0
False
>>> 
>>> 
>>> 
>>> 
============ RESTART: D:/199/8_7/2023/leap_year.py ===========
Enter am year: 1900
1900 isn't leap
>>> 
============ RESTART: D:/199/8_7/2023/leap_year.py ===========
Enter am year: 2016
2016 is leap
>>> 
============ RESTART: D:/199/8_7/2023/leap_year.py ===========
Enter am year: 2000
2000 is leap
>>> 
============ RESTART: D:/199/8_7/2023/leap_year.py ===========
Enter am year: 200
200 isn't leap
>>> 
>>> 
>>> 
>>> 
>>> x = 1900
