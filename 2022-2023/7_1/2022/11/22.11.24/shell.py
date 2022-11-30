Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x = 45
y = 58
print(x, "+", y, "=", x+y)
45 + 58 = 103
45 + 58 = 103
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?


print(f"{x} + {y} = {x + y}")
45 + 58 = 103

print(f"{} + {} = {}")
SyntaxError: f-string: empty expression not allowed

import math as m
r = 3.8945125
length = 2 * m.pi * r
area = m.pi * r **2

print(f"The length is {length} and the area is {area}")
The length is 24.46994371862724 and the area is 47.64925084324513

print(f"The length is {round(length, 2)} and the area is {round(area, 2)}")
The length is 24.47 and the area is 47.65

print(f"The length is {length:.2f} and the area is {area:.2}")
The length is 24.47 and the area is 4.8e+01
print(f"The length is {length:.2f} and the area is {area:.2e}")
The length is 24.47 and the area is 4.76e+01
print(f"The length is {length:.2f} and the area is {area:.2f}")
The length is 24.47 and the area is 47.65


x, y = 45, 58
print(f"{x}{y}")
4558
print(f"{x} {y}")
45 58
print(f"{x:.2f}")
45.00
x
45

print(f"{x:10d}{y:10d}")
        45        58

>>> print(f"{x:<10d}{y:<10d}")
45        58        
>>> 
>>> print(f"{x:<010d}{y:<010d}")
45000000005800000000
>>> print(f"{x:*<10d}{y:*<10d}")
45********58********
>>> 
>>> print(f"{x:*>10d}{y:*>10d}")
********45********58
>>> 
>>> print(f"{' ':<3s}{'Player':<20s}{'Country':<20s}{\"Rating\":<20s}{'Age'}")
SyntaxError: f-string expression part cannot include a backslash
>>> print(f"{' ':<3s}{'Player':<20s}{'Country':<20s}{'Rating':<20s}{'Age'}")
   Player              Country             Rating              Age
>>> 
>>> print(f"{' ':<3s}{'Player':<20s}{'Country':<20s}{'Rating':<20s}{'Age'}\n{'-' * 69}")
   Player              Country             Rating              Age
---------------------------------------------------------------------
>>> 
>>> 
>>> result = f"{' ':<3s}{'Player':<20s}{'Country':<20s}{'Rating':<20s}{'Age'}\n{'-' * 69}"
>>> print(result)
   Player              Country             Rating              Age
---------------------------------------------------------------------
