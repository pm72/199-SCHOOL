x1, y1 = eval(input("Enter first point's coordinates: "))
x2, y2 = eval(input("Enter second point's coordinates: "))
radius = eval(input("Enter a radius: "))

distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

if radius >= distance:
  print("The point is inside in the circle")
else:
  print("The point is outside in the circle")
