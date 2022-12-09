Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import math as m
m.pi
3.141592653589793
# a =  2 * r * m.sin(m.pi / 5)
# m.sqrt()  sqrt()  a ** 0.5   a ** (1/2)


x = 2.589654525
print(round(x, 2))
2.59

print(f"The area of the pentagon is x")
The area of the pentagon is x
print(f"The area of the pentagon is {x}")
The area of the pentagon is 2.589654525
print(f"The area of the pentagon is {x:.2}")
The area of the pentagon is 2.6
print(f"The area of the pentagon is {x:.2f}")
The area of the pentagon is 2.59



x1, y1 = 39.55, -116.25
x1 = m.radians(x1)
y1 = m.radians(y1)

x1, y1
(0.6902777191637572, -2.028945255443408)
m.sin(x1), m.sin(y1)
(0.636751347470152, -0.8968727415326884)

# arccos()   ====> m.acos()   arcsin   ===>  m.asin()  ...

m.degrees(x1), m.degrees(y1)
(39.55, -116.25)



# a = m.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
# b = ... c = ... d = ... e = ...
# p1 = (a + b + e) / 2
# p2 = ...
# s1 = m.sqrt(p * (p - a) * (p - b) * (p - e))
# s2 = ...
# s = s1 + s2



# tan()   ===> m.tan()



# chr()    ord()
chr(69)
'E'
chr(65)
'A'
chr(97)
'a'

ord('A')
65
ord('a')
97
ord('a') - ord('A')
32
ord('r') - ord('R')
32
>>> 
>>> 
>>> 
>>> 
>>> from time import time
>>> time()
1670562304.7341619
>>> int(time())
1670562335
>>> int(time())
1670562336
>>> int(time())
1670562339
>>> 
>>> # [65 .. 90]
>>> 
>>> 
>>> 
>>> |# print("Deductions:")
SyntaxError: invalid syntax
>>> 
>>> # print("Deductions:")
>>> # print("\tFederal Withholding (20.0%): $19.5")
>>> 
>>> 
>>> 
>>> x = 1005
