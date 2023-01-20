import math as m

r = -1

while r < 0:
  r = eval(input("Enter a radius: "))

##if r < 0:
##    print("Wrong input. Enter a positive number.")
##else:
##  area = m.pi * r ** 2
##  
##  print(f"The area is {area:.2f}")

area = m.pi * r ** 2
print(f"The area is {area:.2f}")
