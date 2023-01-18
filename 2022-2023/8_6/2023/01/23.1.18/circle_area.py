'''
  if piroba:
    line 1
    line 2
    ...
    line n
  else:
    line 10
    line 20
    ...
    line n
'''

import math as m

r = eval(input("Enter a radius: "))

##if r < 0:
##  print("Wrong answer. Enter a positive number!")
##else:
##  area = m.pi * r ** 2
##
##  print(f"The area is {area:.2f}")

if r > 0:
  area = m.pi * r ** 2
  print(f"The area is {area:.2f}")
