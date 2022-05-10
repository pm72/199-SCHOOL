import turtle

s = turtle.getscreen()
t = turtle.Turtle()

turtle.title("Computing distances")
turtle.setup(800, 500)
turtle.bgcolor("darkviolet")

t.ht()
turtle.ht()

x1 = turtle.numinput("Point 1 coords", "Enter x1 for point 1:")
y1 = turtle.numinput("Point 1 coords", "Enter y1 for point 1:")

x2 = turtle.numinput("Point 2 coords", "Enter x2 for point 2:")
y2 = turtle.numinput("Point 2 coords", "Enter y2 for point 2:")

distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

t.pencolor('white')
t.pensize(3)

t.pu()
t.goto(x1, y1)
t.pd()
t.dot(10)
t.write(f"Point 1 ({x1}, {y1})", font=("calibri", 12, 'bold'))

t.goto(x2, y2)
t.dot(10)
t.write(f"Point 2 ({x2}, {y2})", font=("calibri", 12, 'bold'))

t.pu()
t.goto((x1 + x2) / 2, (y1 + y2) / 2)
t.pd()
t.dot(10)
t.write(f"Distance: {d.istance:2f}", font=("calibri", 12, 'bold'))


# =====================
turtle.exitonclick()