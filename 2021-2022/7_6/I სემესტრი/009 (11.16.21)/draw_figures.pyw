import turtle

s = turtle.getscreen()
t = turtle.Turtle()

t.speed(1)

'''
forward()    =>  fd()
backward()   =>  bk()
left         =>  lt()
right        =>  rt()
'''

##a = 150
##
##t.fd(a)
##
##t.lt(120)
##t.fd(a)
##
##t.home()


##t.goto(0, 100)
##t.goto(100, 100)
##t.goto(100, 0)
##t.goto(0, 0)

##a = 100
##
##t.penup()
##t.goto(-a/2, -a/2)
##
##t.pendown()
##t.goto(-a/2, a/2)
##t.goto(a/2, a/2)
##t.goto(a/2, -a/2)
##t.goto(-a/2, -a/2)

r = 50

t.penup()
t.goto(0, -r)

t.pendown()
t.circle(r)




# ==============
t.hideturtle()
turtle.hideturtle()

turtle.done()
