import math as m

radius = eval(input("Enter radius: "))

##if radius < 0:
##  print("Wrong input, enter positive number!..")
##else:
##  area = m.pi * radius ** 2
##  print(f"the area is {area:.2f}")


if radius >= 0:
  area = m.pi * radius ** 2
  print(f"the area is {area:.2f}")
