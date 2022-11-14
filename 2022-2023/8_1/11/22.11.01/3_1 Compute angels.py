##import math as m
from math import sqrt, pow, acos, degrees

x1, y1, x2, y2, x3, y3 = eval(input("Enter three points: "))

a = sqrt(pow(x2 - x3, 2) + pow(y2 - y3, 2))
b = sqrt(pow(x1 - x3, 2) + pow(y1 - y3, 2))
c = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))

A = degrees(acos((a * a - b * b - c * c) / (-2 * b * c)))
B = degrees(acos((b * b - a * a - c * c) / (-2 * a * c)))
C = degrees(acos((c * c - b * b - a * a) / (-2 * a * b)))

print("The three angles are", round(A, 2), round(B, 2), round(C, 2))
