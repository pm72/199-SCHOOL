# s = pi * r ** 2    pi = 3.14159...
# l = 2 * pi * r
# int('15') = 15  float('2.9') = 2.9  float('1') = 1.0
# eval('25') = 25   eval('2.98') = 2.98   
# round(value[, x])  round(15.892) = 16   round(15.896, 2) = 15.9

try:
  radius = eval(input("Enter the radius: "))
  PI = 3.14159

  area = PI * radius ** 2
  perimeter = 2 * PI * radius

  print("The area of the circle of radius", radius,
        "is", round(area, 2))
  print("The perimeter of the circle of radius", radius,
        "is", round(perimeter, 2))


  input()
except SyntaxError as error:
  error = "Illegeal input.\nPlease enter the valid number."
  print(error)

  input()
