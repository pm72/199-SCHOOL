import math as m

radius = eval(input("Enter a radius: "))
area = 0

##if radius < 0:
##  print("Wrong input, enter positive number.")
##else:
##  area = m.pi * radius ** 2
##  
##print(f"The area is {area:.2f}")


if radius > 0:
  area = m.pi * radius ** 2
  
print(f"The area is {area:.2f}")



#  if .. else
