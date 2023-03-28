x1, y1, x2, y2 = eval(input("Enter two point's coordinates, separated by commas: "))
radius = eval(input("Enter a radius: "))

distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

if distance <= radius:
  print("The point is inside the circle")
else:
  print("The point is outside the circle")
