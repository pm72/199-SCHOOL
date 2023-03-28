x, y = eval(input("Enter point's coordinates: "))
w, h = eval(input("Enter rectangles width and height: "))

if x <= w / 2 and y <= h / 2:
  print("Point is inside the rectangle")
else:
  print("Point is outside the rectangle")
