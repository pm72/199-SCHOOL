import turtle
from dynamic_math import dynamic_math

t = turtle.Turtle()
s = turtle.getscreen()

turtle.title("მათემატიკური ოპერაციები")
turtle.setup(width=1200, height=600)
turtle.bgcolor('lightcyan')

t.ht()
turtle.ht()

dynamic_math(1.089, 2.301, '/', "#fd045f")
dynamic_math(57, 129, '*', "#aabb58")
dynamic_math(189, 93, '+', "#004521")
dynamic_math(18.09, 9.83, '**', "#a5e4d1")

num1 = turtle.numinput("", "რიცხვი 1:")
num2 = turtle.numinput("", "რიცხვი 2:")
dynamic_math(num1, num2, '/', '#d4e215')



# =================
turtle.exitonclick()