import math as m

x1, y1, x2, y2, x3, y3 = eval(input("Enter three points: "))

a = m.sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)
b = m.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
c = m.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

A = m.degrees(m.acos((a * a - b * b - c * c) / (-2 * b * c)))
B = m.degrees(m.acos((b * b - a * a - c * c) / (-2 * a * c)))
C = m.degrees(m.acos((c * c - b * b - a * a) / (-2 * a * b)))

print("The three angles are", round(A, 2), round(B, 2), round(C, 2))
