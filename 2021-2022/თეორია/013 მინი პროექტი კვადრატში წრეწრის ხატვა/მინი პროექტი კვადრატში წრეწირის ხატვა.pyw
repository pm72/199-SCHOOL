import turtle

s = turtle.getscreen()
t = turtle.Turtle()

turtle.title("Python turtle - Circle within a Square")

t.speed(5)

# Set the color and pen size for the square
t.fillcolor('red')
t.pensize(5)

# Draw the square
t.penup()
t.goto(-100, -100)
t.pendown()

t.begin_fill()
t.goto(-100, 100)
t.goto(100, 100)
t.goto(100, -100)
t.goto(-100, -100)
t.end_fill()

# Set position so the circle's center is 0,0
t.penup()
t.goto(0, -100)
t.pendown()

# Draw the circle
# Color and size
t.fillcolor('blue')

t.begin_fill()
t.circle(100)
t.end_fill()




# =================
t.hideturtle()
turtle.hideturtle()
turtle.done()
