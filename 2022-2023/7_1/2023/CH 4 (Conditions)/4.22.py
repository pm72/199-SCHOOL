w, h = eval(input("Enter rectangle's width and height: "))
x, y = eval(input("point's coordinates: "))

if x <= w / 2 and y <= h / 2:
  print(f"Point ({x}, {y}) is inside the treangle")
else:
  print(f"Point ({x}, {y}) is outside the treangle")
