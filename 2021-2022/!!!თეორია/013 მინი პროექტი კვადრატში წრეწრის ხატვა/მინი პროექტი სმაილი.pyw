import turtle

s = turtle.getscreen()
t = turtle.Turtle()

turtle.title("Python turtle – Mini Project: Smiley")

# Let's draw a smiley
# Go to the position
t.penup()
t.goto(0, -100)
t.pendown()

# Draw the face
# Color and size
t.fillcolor('yellow')
t.pensize(5)

# Circle
t.begin_fill()
t.circle(100)
t.end_fill()

# Draw the eyes
# First eye
t.penup()
t.goto(-40, 30)
t.pendown()
t.dot(30)

# Second eye
t.penup()
t.goto(40, 30)
t.pendown()
t.dot(30)

# Draw the noce
t.penup()
##t.goto(0,0)
t.home()
t.pendown()
t.goto(0, -30)

# Draw the smile
# Go to the x position of the eye but a different y position
t.penup()
t.goto(-35, -40)
t.pendown()

# Change the direction of the pen (turtle)
t.setheading(-60)
t.circle(40, 120)




# =================
t.hideturtle()
turtle.hideturtle()
turtle.done()
