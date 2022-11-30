Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import math as m
m.pi
3.141592653589793
m.sqrt(16)
4.0
16 ** 0.5
4.0
pow(2, 3)
8
m.pow(2, 3)
8.0


m.degrees(m.pi)
180.0
m.degrees(m.pi / 2)
90.0
m.degrees(2 * m.pi)
360.0
m.degrees(2 * m.pi + 1)
417.2957795130823

m.radians(90)
1.5707963267948966
m.pi / 2
1.5707963267948966



m.degrees(60)
3437.746770784939
60 * (180 / m.pi)
3437.746770784939



help(m.acos)
Help on built-in function acos in module math:

acos(x, /)
    Return the arc cosine (measured in radians) of x.
    
    The result is between 0 and pi.


============ RESTART: D:/199/8_5/22.11.17/Compute angles.py ============
Enter three points: 1, 1, 6.5, 1, 6.5, 2.5
Tha angles are: 0.27 1.57 1.3
>>> are: 0.27 1.57 1.3
SyntaxError: invalid syntax
>>> 

>>> 0.27 + 1.57 + 1.3
3.14
>>> 
============ RESTART: D:/199/8_5/22.11.17/Compute angles.py ============
Enter three points: 1, 1, 6.5, 1, 6.5, 2.5
Tha angles are: 15.26 90.0 74.74
>>> 
============ RESTART: D:/199/8_5/22.11.17/Compute angles.py ============
Enter three points: 1, 1, 6.5, 1, 6.5, 2.5
Tha angles are: 15.26 ° 90.0 ° 74.74 °
>>> 
============ RESTART: D:/199/8_5/22.11.17/Compute angles.py ============
Enter three points: 1, 1, 6.5, 1, 6.5, 2.5
Tha angles are: 15.26'°' 90.0'°' 74.74'°'
>>> 
============ RESTART: D:/199/8_5/22.11.17/Compute angles.py ============
Enter three points: 1, 1, 6.5, 1, 6.5, 2.5
Tha angles are: 15.26° 90.0° 74.74°
>>> 
============ RESTART: D:/199/8_5/22.11.17/Compute angles.py ============
Enter three points: 1, 1, 6.5, 1, 6.5, 2.5
Tha angles are: 15.26° 90.0° 74.74°
