import turtle

s = turtle.getscreen()
t = turtle.Turtle()

turtle.title("Drawing smiley")
turtle.bgcolor("#961287")

t.speed(10)
t.pensize(5)
t.fillcolor("yellow")


# Go to pozition
t.penup()
t.goto(0, -100)
t.pendown()


# Drawing face
t.begin_fill()
t.circle(100)
t.end_fill()


# Go to position and draw first eye
t.penup()
t.goto(-40, 30)
t.pendown()

t.dot(30)


# Go to position and draw second eye
t.penup()
t.goto(40, 30)
t.pendown()

t.dot(30)


# Go to position and draw the nose
t.penup()
t.home()
t.pendown()

t.goto(0, -30)


# Draw smile
t.setheading(-60)
t.penup()
t.goto(-35, -40)
t.pendown()

t.circle(40, 120)


##t.setheading(120)
##t.penup()
##t.goto(35, -70)
##t.pendown()
##
##t.circle(40, 120)


##t.setheading(0)
##t.penup()
##t.goto(-25, -50)
##t.pendown()
##
##t.forward(50)




# ======================
t.hideturtle()
turtle.hideturtle()
turtle.done()
