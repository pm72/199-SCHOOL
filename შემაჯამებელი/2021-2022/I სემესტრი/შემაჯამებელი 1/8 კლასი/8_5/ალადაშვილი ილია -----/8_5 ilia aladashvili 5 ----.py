Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x1=int(input())
x2=int(input())
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    x1=int(input())
ValueError: invalid literal for int() with base 10: 'x2=int(input())'
y1=int(input())
y2=int(input())
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    y1=int(input())
ValueError: invalid literal for int() with base 10: 'y2=int(input())'


print(math.sqrt(pow(x2-x1,2) + pow(x2 - x1,2)))
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print(math.sqrt(pow(x2-x1,2) + pow(x2 - x1,2)))
NameError: name 'math' is not defined
