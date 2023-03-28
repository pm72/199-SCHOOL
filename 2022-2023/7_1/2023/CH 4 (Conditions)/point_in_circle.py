x1, y1 = eval(input("Enter first point's coordinates x1 and y1: "))
x2, y2 = eval(input("Enter second point's coordinates x2 and y2: "))

radius = -1
while radius <= 0:
  radius = eval(input("Enter the radius: "))

distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
distance = round(distance, 2)

if distance <= radius:
  print("The point is inside the circle")
else:
  print("The point is outside the circle")
