import turtle

s = turtle.getscreen()
t = turtle.Turtle()

turtle.title("Draw a circle")
turtle.setup(800, 500)
turtle.bgcolor("lightblue")

t.ht()
turtle.ht()

x = turtle.numinput("x coord for circles center", "Enter x coord:")
y = turtle.numinput("y coord for circles center", "Enter y coord:")
r = turtle.numinput("Circle radius", "Radius:")

t.pu()
t.goto(x=x, y=y)
t.pd()

t.pencolor('darkred')
t.pensize(5)
t.fillcolor('blue')

t.begin_fill()
t.circle(r)
t.end_fill()

t.pencolor('white')

area = f"The area:\n{(3.14 * r ** 2):.2f}"

t.pu()
t.goto(x, y + 0.75 * r)
t.pd()
t.write(area, font=('georgia', 15, 'bold'), align='center')


# =====================
# turtle.exitonclick()
turtle.done()