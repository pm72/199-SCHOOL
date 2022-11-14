# s = pi * r ** 2    pi = 3.14159...
# l = 2 * pi * r

radius = eval(input("Enter the radius: "))    # '25'  '2.36'
PI = 3.14159

area = round(PI * radius ** 2, 2)
perimeter = round(2  * PI * radius, 2)

print("The area of the circle of radius", radius, "is", area)
print("The perimeter of the circle of radius", radius, "is", perimeter)
