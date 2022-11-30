Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x, y = 45, 58
print(x, y)
45 58

print(f"{x} {y}")
45 58

print(f"{x} + {y} = {x + y}")
45 + 58 = 103


x = 2.8941
y = 0.9587445
print(f"{x / y}")
3.0186353089900386

print(f"{(x / y):.2
      }")
SyntaxError: unterminated string literal (detected at line 1)
>>> 
>>> print(f"{(x / y):.2}")
3.0
>>> 
>>> print(f"{(x / y):.2f}")
3.02
>>> 
>>> 
>>> print(f"{x:.2f}{y:.2f}")
2.890.96
>>> 
>>> print(f"{x:10.2f}{y:10.2f}")
      2.89      0.96
>>> 
>>> print(f"{x:010.2f}{y:10.2f}")
0000002.89      0.96
>>> 

>>> print(f"{x:*>10.2f}{y:*>10.2f}")
******2.89******0.96
>>> 
>>> print(f"{x:*<10.2f}{y:*<10.2f}")
2.89******0.96******
>>> 
============= RESTART: D:/199/8_7/22.11.25/display_info.py =============
   Player              Country             Rating              Age
---------------------------------------------------------------------
