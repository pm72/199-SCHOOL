Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import math

x1 = float(input("Sheiyvanet x1: "))
x2 = float(input("Sheiyvanet x2: "))
y1 = float(input("Sheiyvanet y1: "))
y2 = float(input("Sheiyvanet y2: "))

dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(dist)