Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import math as m
help(m.acos)
Help on built-in function acos in module math:

acos(x, /)
    Return the arc cosine (measured in radians) of x.
    
    The result is between 0 and pi.


========== RESTART: D:/199/7_7/22.11.10/3_1 Compute Angeles.py ==========
Enter three points: 1, 1, 6.5, 1, 6.5, 2.5
The three angles are  0.27 1.57 1.3


m.degrees(m.pi)
180.0
m.degrees(m.pi/2)
90.0
m.radians(90)
1.5707963267948966

========== RESTART: D:/199/7_7/22.11.10/3_1 Compute Angeles.py ==========
Enter three points: 1, 1, 6.5, 1, 6.5, 2.5
The three angles are  15.26 90.0 74.74


m.degrees(1.57)
89.95437383553924



round(-2.5)
-2
round(2.5)
2



rad = m.radians(47)
rad
0.8203047484373349

m.degrees(m.pi / 7)
25.714285714285715



'4'
'4'
type('4')
<class 'str'>
type("4")
<class 'str'>
type("Good Morninig")
<class 'str'>
type('Good Morninig')
<class 'str'>

2**16
65536



# ord()  chr()

ord('A')
65
>>> ord('a')
97
>>> 
>>> ord('Z')
90
>>> ord('z')
122
>>> 
>>> chr(68)
'D'
>>> chr(68+32)
'd'
>>> 
>>> ord('a') = ord('A')
SyntaxError: cannot assign to function call here. Maybe you meant '==' instead of '='?
>>> ord('a') - ord('A')
32
>>> ord('k') - ord('K')
32
>>> 
>>> 
>>> 
>>> print("cos(\u03b1 + \u03b2)")
cos(α + β)
>>> print("cos(α + β) = 2.459")
cos(α + β) = 2.459
