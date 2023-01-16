import math as m

radius = eval(input("Enter a radius: "))

if radius < 0:
  print("Error! Enter a positive number...")
else:
  print(f"The are is {(m.pi * radius ** 2):.2f}")
