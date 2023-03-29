'''
    if condition:
      statment 1
      statment 2
      ...
      statment n
    else:
      statment 10
      statment 20
      ...
      statment n
'''

import math as m

r = eval(input("Enter a radius: "))
area = 0

if r < 0:
  print("Wrong input. Enter a positive number.")
else:
  area = m.pi * r ** 2
  print(f"The area is {area:.2f}")


print("\nDone!\n\n")

##if r > 0:
##  area = m.pi * r ** 2
##
##print(f"The area is {area:.2f}")
##
##
##d = m.sqrt(area) * 2.569
##print(f"d = {d}")
##
##print("\nDone!\n\n")


