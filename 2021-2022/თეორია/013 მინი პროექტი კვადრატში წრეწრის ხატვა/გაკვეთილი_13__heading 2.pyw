import turtle

s = turtle.getscreen()
t = turtle.Turtle()

turtle.title("Python turtle - Change Directions of your Drawing")

print(t.heading())

t.pensize(5)
t.speed(5)

t.forward(100)
t.write(t.heading())
t.penup()
t.home()
t.pendown()

# 90 degrees
t.setheading(90)
t.forward(100)
t.write(t.heading())
t.penup()
t.home()
t.pendown()

# 180 degrees
t.setheading(180)
t.forward(100)
t.write(t.heading())
t.penup()
t.home()
t.pendown()

# 270 degrees
t.setheading(270)
t.forward(100)
t.write(t.heading())
t.penup()
t.home()
t.pendown()




# =================
##t.hideturtle()
##turtle.hideturtle()
turtle.done()
