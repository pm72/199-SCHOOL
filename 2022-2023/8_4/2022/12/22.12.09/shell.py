Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import math as m
m.pi
3.141592653589793
m.sin(m.pi / 5)
0.5877852522924731
_ * 5.5 * 2
6.465637775217204

area = 108.614584136
print("The area of the pentagon is", round(area, 2))
The area of the pentagon is 108.61
print("The area of the pentagon is
      )
SyntaxError: unterminated string literal (detected at line 1)
"
SyntaxError: unterminated string literal (detected at line 1)


print(f"The area of the pentagon is area")
The area of the pentagon is area
print(f"The area of the pentagon is {area}")
The area of the pentagon is 108.614584136
print(f"The area of the pentagon is {area:.2}")
The area of the pentagon is 1.1e+02
print(f"The area of the pentagon is {area:.2f}")
The area of the pentagon is 108.61
print(f"The area of the pentagon is {area:.f}")
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    print(f"The area of the pentagon is {area:.f}")
ValueError: Format specifier missing precision
print(f"The area of the pentagon is {area:.0f}")
The area of the pentagon is 109



x1, y1 = 39.55, -116.25
x1 = m.radians(x1)
y1 = m.radians(y1)
x1, y1
(0.6902777191637572, -2.028945255443408)
(0.6902777191637572, -2.028945255443408)
(0.6902777191637572, -2.028945255443408)

m.sin(x1), m.cos(y1)
(0.636751347470152, -0.44228869021900113)


# arcos()   m.acos()    arcsin()   ====> m.asin()



# a = m.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
# b, c, d, e = ...

# p1 = (a + b + e) / 2
# p2 = ...

# s1 = m.sqrt(p1 * (p1 - a) * (p1 - b) * (p1 - e))
# s2 = ...
# s = s1 + s2


# tan()   ===> m.tan()


# chr()   # ord()
chr(69)
'E'
chr(65)
'A'
chr(97)
'a'

ord('a')
97
ord('a') - ord('A')
32
ord('s') - ord('S')
32
>>> 
>>> 
>>> 
>>> 
>>> from time import time
>>> time()
1670581570.7760901
>>> int(time())
1670581601
>>> int(time())
1670581603
>>> int(time())
1670581604
>>> int(time())
1670581605
>>> 
>>> 
>>> #  [65 .. 90]
>>> 
>>> 
>>> 
>>> # print("Deductions:")
>>> # print(f"\tFederal Withholding ({dd}%): ${ss:.2f}")
>>> 
>>> 
>>> 
>>> x = 1005
