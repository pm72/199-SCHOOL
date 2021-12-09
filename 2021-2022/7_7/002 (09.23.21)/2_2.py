Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = 34
>>> 
>>> 
>>> 5+9
14
>>> 
>>> 
>>> range(1,10)
range(1, 10)
>>> *range(1, 10)
SyntaxError: can't use starred expression here
>>> print(*range(1, 10))
1 2 3 4 5 6 7 8 9
>>> print(*range(1, 11))
1 2 3 4 5 6 7 8 9 10
>>> x = 12
>>> x
12
>>> x = 10
>>> x
10
>>> x = "Paata"
>>> x
'Paata'
>>> print(*range(1, 21, 2))
1 3 5 7 9 11 13 15 17 19
>>> for i in range(10):  # for (int i = 0; i < 10; i++)
	print(i)

	
0
1
2
3
4
5
6
7
8
9
>>> 