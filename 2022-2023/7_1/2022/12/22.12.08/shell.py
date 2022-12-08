Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import math as m
m.pi
3.141592653589793
##a = 2 * r *  m.sin(m.pi / 2)

m.sqrt(3)
1.7320508075688772

x = 2.8912584
print(round(x, 2))
2.89
print(f"{x}")
2.8912584
print(f"{x:.2
      }")
SyntaxError: unterminated string literal (detected at line 1)
print(f"{x:.2}")
2.9
print(f"{x:.2f}")
2.89




x1, y1 = 39.55, -116.25
x1 = m.radians(x1)
y1 = m.radians(y1)

x1
0.6902777191637572
y1
-2.028945255443408

#  arccos()  ===> m.acos()   arcsin()  ===> m.asin()

m.sin(x1)
0.636751347470152
a.sin(y1)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    a.sin(y1)
NameError: name 'a' is not defined
m.sin(y1)
-0.8968727415326884



# a = m.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)  5-jer
# p1 = (a + b + e) / 2
# p2 = ...
# s1 = m.sqrt(p * (p - a) * (p - b) * (p - e))
# s2 = ...
# s = s1 + s2


# tan()   ====> m.tan(m.pi / 5 )


# chr()    ord()
chr(69)
'E'
chr(65)
'A'
chr(97)
'a'

ord('a')
97
ord('A')
65

>>> ord('a') - ord('A')
32
>>> ord('f') - ord('F')
32
>>> 
>>> 
>>> from time import time
>>> time()
1670476171.951762
>>> int(time())
1670476202
>>> 1670476202
1670476202
>>> 
>>> 1670476202
1670476202
>>> int(time())
1670476221
>>> int(time())
1670476222
>>> int(time())
1670476226
>>> 
>>> 
>>> # [65..90]
>>> 
>>> 
>>> 
