Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s = "welcome to python"
s.upper()
'WELCOME TO PYTHON'
s
'welcome to python'

s = s.upper()
s
'WELCOME TO PYTHON'

s.lower()
'welcome to python'
s
'WELCOME TO PYTHON'

s = s.lower()
s
'welcome to python'

s.title()
'Welcome To Python'

s = s.title()
s
'Welcome To Python'

s.capitalize()
'Welcome to python'

s = s.capitalize()
s
'Welcome to python'


s = "     welcome to python         "
s
'     welcome to python         '
s.strip()
'welcome to python'
s
'     welcome to python         '
s=s.strip()
s
'welcome to python'


s = "<strong>welcome</strong>"
s.strip('<strong>')
'welcome</'
s.strip('</')
'strong>welcome</strong>'


s = s.strip('<strong> </')
s
'welcome'


s.strip()      # ' '  '\n'  '\t'  '\r'  '\f'
'welcome'


help(strip)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    help(strip)
NameError: name 'strip' is not defined
help(s.strip)
Help on built-in function strip:

strip(chars=None, /) method of builtins.str instance
    Return a copy of the string with leading and trailing whitespace removed.
    
    If chars is given and not None, remove characters in chars instead.



s
'welcome'
s.strip('w')
'elcome'
s.strip('c')
'welcome'
s.strip('e')
'welcom'
s.strip('me')
'welco'


s = '   welcome'
s.strip(s.title())
'w'


s = s.strip()
s.title()
'Welcome'


k = 9
k.strip()
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    k.strip()
AttributeError: 'int' object has no attribute 'strip'


str(k).strip()
'9'
k
9


(str(k) + '   ').strip()
'9'
(str(k) + '   ')
'9   '
_.strip()
'9'


id(k)
1324414140912
id('loma')
1324455268656

type(k)
<class 'int'>


n = 3


'\tGeorgia\n'.upper()
'\tGEORGIA\n'


" \tGood\tMorning\n".strip()     # Good\tMorning
'Good\tMorning'
print(" \tGood\tMorning\n".strip())
Good	Morning



x = 12.85745
print(round(x, 2))
12.86

print("x =", round(x, 2))
x = 12.86

print(f"x = {x}")
x = 12.85745

a = 5
b = 7
print(a, "+", b, "=", a + b)
5 + 7 = 12
print(f"{a} + {b} = {a + b}")
5 + 7 = 12


print(f"x = {x:.2f}")
x = 12.86
print(f"x = {x:2d}")
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    print(f"x = {x:2d}")
ValueError: Unknown format code 'd' for object of type 'float'
>>> 
>>> print(f"x = {x:.2d}")
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    print(f"x = {x:.2d}")
ValueError: Unknown format code 'd' for object of type 'float'
>>> 
>>> y = 15
>>> print(f"x = {y:.2f}")
x = 15.00
>>> x = 15.00
>>> 
>>> 
>>> print(f"x = {x:.2f}, y = {y:.2f}")
x = 15.00, y = 15.00
>>> 
>>> 
>>> 12.85745
12.85745
>>> print(f"x = {x:.2f}, y = {y:.2f}")
x = 15.00, y = 15.00
>>> 
>>> 
>>> x = 12.85745
>>> print(f"x = {x:.2f}, y = {y:.2f}")
x = 12.86, y = 15.00
>>> 
>>> 
