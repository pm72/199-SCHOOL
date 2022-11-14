Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> x, y, z = 12, 52, 21
>>> x
12
>>> y
52
>>> z
21
>>> 
>>> a, b, c = eval(input("Enter three numbers:"))
Enter three numbers:58 63 24
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    a, b, c = eval(input("Enter three numbers:"))
  File "<string>", line 1
    58 63 24
        ^
SyntaxError: invalid syntax
>>> a, b, c = eval(input("Enter three numbers deparated by commas:"))
Enter three numbers deparated by commas:25, 63, 0
>>> a, b, c
(25, 63, 0)
>>> (a + b + c) / 3
29.333333333333332
>>> '1 + 2'
'1 + 2'
>>> 1 + 2
3
>>> \


  
>>> 
>>> 8 / 5
1.6
>>> 8 / 2
4.0
>>> 
>>> 5 + 8 / 2
9.0
>>> 
>>> 
>>> 7 + 1.5
8.5
>>> 7 + 1.0
8.0
>>> int(7 + 8 / 4)
9
>>> 
>>> 
>>> 8 // 5
1
>>> 8 // 4
2
>>> 19 // 7
2
>>> 8 5 5
SyntaxError: invalid syntax
>>> 8 % 5
3
>>> 29 % 6
5
>>> 12 % -5
-3
>>> -12 % 5
3
>>> -(12 % 5)
-2
>>> 
>>> 
>>> s = 0
>>> 
>>> s + 1
1
>>> s = s + 1
>>> s
1
>>> s = s + 1
>>> s
2
>>> s += 1
>>> s
3
>>> s+=10
>>> s
13
>>> s -= 10
>>> s
3
>>> s *= 5
>>> s
15
>>> s /= 5
>>> s
3.0
>>> s = 15
>>> 
>>> s //= 5
>>> s
3
>>> s %= 8
>>> s
3
>>> 
>>> s %= 3
>>> s
0
>>> 
>>> s %= 7
>>> s
0
>>> 
>>> 
>>> x = 45
>>> reverse_x = x % 10 * 10 + x // 10 * 1
>>> reverse_x
54
>>> reverse_x * 5
270
>>> 
