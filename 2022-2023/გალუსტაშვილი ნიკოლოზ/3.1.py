import math as m

r = eval(input("Enter the length from the center to a vertex: "))

a = 2 * r * m.sin(m.pi / 5)

area = 3 * m.sqrt(3) / 2 * a ** 2

print(f"The area of the pentagon is {area:.2f}")
