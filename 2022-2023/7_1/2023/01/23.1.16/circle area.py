# if .. else      if .. elif .. elif .. .. else

import math as m

radius = eval(input("Enter a radius: "))

if radius < 0:
  print("ERROR! Enter a positive number!")
  print("Negative")
else:
  print(f"The area of the circle is {(m.pi * radius ** 2):.2f}")
