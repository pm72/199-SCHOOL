## წრის ფართობი:  s = pi * r * r, სადაც pi = 3.14159
## წრეწირის სიგრძე (პერიმეტრი): l = 2 * pi * r
# round(value[, x])   round(2.892544) = 3  round(2.592544, 2) = 2.59
# input()

radius = eval(input("Enter the radius: "))
PI = 3.14189

area = round(PI * radius ** 2, 2)
length = round(2 * PI * radius, 2)

print("The area of the circle width radius", radius, "is", area)
print("The length of the circle width radius", radius, "is", length)



## ინფორმაცია
## ტექსტი   string   პითონში str
##
## რიცხვითი:   მთელი int, ათწილადი float
## int 5 8 9 0 -69 55 ...
## float 1.89 6.0589 -5.2147  1.0


# int('2') = 2   int('-8') = -8
# float('2.58') = 2.58   float('1') = 1.0
# int(7.89) = 7   float(5) = 5.0
# eval('1.25') = 1.25   eval(25) = 25
