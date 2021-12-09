import turtle

s = turtle.getscreen()
t = turtle.Turtle()

t.speed(8)

##a = 150
##
##t.penup()
##t.goto(-a/2, -a/2)
##
##t.pendown()
##t.goto(-a/2, a/2)
##t.goto(a/2, a/2)
##t.goto(a/2, -a/2)
##t.goto(-a/2, -a/2)
##
##t.penup()
##t.home()
##t.dot()


##t.circle(100)
##t.circle(-100)
##
##t.penup()
##t.goto(0, 100)
##t.dot()
##
##t.goto(0, -100)
##t.dot()
##
##t.pendown()
##t.goto(0, 100)

##t.circle(100, 90)

a = 150
angle = 20


t.fd(a)
t.circle(angle, 180)

t.fd(a)
t.circle(angle, 180)



# ==============
t.hideturtle()
turtle.hideturtle()

turtle.done()
