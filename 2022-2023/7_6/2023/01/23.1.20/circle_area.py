import math as m

r = eval(input("Enter a radius: "))
area = 0

##if r < 0:
##    print("Wrong input. Enter a positive.")
##else:
##  area = m.pi * r ** 2
##  
##  print(f"The area is {area:.2f}")

if r > 0:
  area = m.pi * r ** 2

print(f"The area is {area:.2f}")



print(m.pi / area)
