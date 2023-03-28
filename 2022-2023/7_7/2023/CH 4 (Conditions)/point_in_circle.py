x1, y1 = eval(input("Enter first point's coordinates: "))
x2, y2 = eval(input("Enter second point's coordinates: "))

radius = 0
while radius <= 0:
  radius = eval(input("Enter the radius: "))

distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

if distance <= radius:
  print("Point is inside the circle")
else:
  print("Point is outside the circle")
