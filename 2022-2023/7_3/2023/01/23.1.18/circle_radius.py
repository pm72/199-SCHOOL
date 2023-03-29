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

radius = eval(input("Enter a radius: "))
area = 0

##if radius < 0:
##  print("Wrong input. Enter a positive number!..")
##else:
##  area = m.pi * radius ** 2
##  print(f"The area is {area:.2f}")
##  
##print("\nDone!")


if radius > 0:
  area = m.pi * radius ** 2
  print(f"The area is {area:.2f}")


print("\nDone!\n\n")
