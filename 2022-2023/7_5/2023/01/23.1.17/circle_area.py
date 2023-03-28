import math as m

radius = eval(input("Enter a radius: "))

if radius < 0:
  print("Wrong input. Enter positive number!..")
else:
  area = m.pi * radius ** 2
  print(f"The area is {area:.2f}")
