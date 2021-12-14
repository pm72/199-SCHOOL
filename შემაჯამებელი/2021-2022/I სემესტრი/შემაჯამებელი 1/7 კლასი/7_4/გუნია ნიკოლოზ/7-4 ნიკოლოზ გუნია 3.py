Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
>>> n=
SyntaxError: invalid syntax
>>> n=random.randit(100,999)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    n=random.randit(100,999)
AttributeError: module 'random' has no attribute 'randit'
>>> n=random.randint(100,999)
>>> minute=n//60
>>> second=n%60
>>> print(n, minute, second)
895 14 55
>>> 