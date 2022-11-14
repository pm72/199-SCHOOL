'''
წრის ფართობის ფორმულა: s = pi * r ** 2     pi = 3.14159...
წრეწირის პერიმეტრი, სიგრძე: l = 2 * pi * r


int('15') = 15
float('12.58') = 12.58   float("12") = 12.0
eval('15') = 15   eval("12.5874") = 12.5874
'''

radius = eval(input("Enter the radius: "))
PI = 3.14159

area = PI * radius ** 2
perimeter = 2 * PI * radius

print("The area of the circle is", round(area, 2), "of radius", radius)
print("The perimeter of the circle is", round(perimeter, 2), "of radius", radius)


input()
