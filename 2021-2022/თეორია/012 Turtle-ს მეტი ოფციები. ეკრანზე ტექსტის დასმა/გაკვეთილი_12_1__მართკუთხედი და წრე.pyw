import turtle

s = turtle.getscreen()
t = turtle.Turtle()

turtle.title("Python turtle - Rectangle and circle")

# chaing positions
t.penup()
t.goto(-200, 200)
t.pendown()

t.fillcolor('blue')

# Draw the square
t.begin_fill()
t.goto(-100, 200)
t.goto(-100, 100)
t.goto(-200, 100)
t.goto(-200, 200)
t.end_fill()

# Change positions again
t.penup()
t.goto(200, -200)
t.pendown()

t.fillcolor('red')

# Draw circle radius = 50
t.begin_fill()
t.circle(50)
t.end_fill()



# =================
t.hideturtle()
turtle.hideturtle()
turtle.done()
