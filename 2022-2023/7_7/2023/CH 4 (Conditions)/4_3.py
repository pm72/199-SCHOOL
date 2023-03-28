a, b, c, d, e, f = eval(input("a, b, c, d, e, f: "))

k = a * d - b * c

if k == 0:
  print("No answer!")
else:
  x = (e * d - b * f) / k
  y = (a * f - e * c) / k

  print(f"x is {x:.2f} and y is {y:.2f}")
