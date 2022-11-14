import math as m

x1, y1, x2, y2, x3, y3 = eval(input("Enter three points: "))

a = m.sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)
b = m.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
c = m.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

A = m.degrees(m.acos((a ** 2 - b ** 2 - c ** 2) / (-2 * b * c)))
B = m.degrees(m.acos((b ** 2 - a ** 2 - c ** 2) / (-2 * a * c)))
C = m.degrees(m.acos((c ** 2 - b ** 2 - a ** 2) / (-2 * b * a)))

print("The three angles are", round(A, 2), round(B, 2), round(C, 2))
