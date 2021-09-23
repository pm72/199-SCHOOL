Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> print(25 * 8)
200
>>> 
>>> 
>>> print(range(1, 10))
range(1, 10)
>>> 
>>> print(*range(1, 10))
1 2 3 4 5 6 7 8 9
>>> print(*range(1, 11))
1 2 3 4 5 6 7 8 9 10
>>> 
>>> 
>>> b = *range(1, 11)
SyntaxError: can't use starred expression here
>>> b = range(1, 11)
>>> b
range(1, 11)
>>> print(*b)
1 2 3 4 5 6 7 8 9 10
>>> 