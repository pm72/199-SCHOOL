import turtle

s = turtle.getscreen()
t = turtle.Turtle()

'''
forward   =>  fd
backward   =>  bk
right     =>  rt
left      =>  lt
'''

t.speed(1)

##t.speed(2)
##
##a = 150
##
##t.fd(a)
##
##t.lt(120)
##t.fd(a)
##
##t.home()
##
##t.lt(60)
##t.fd(a)
##
##t.lt(120)
##t.fd(a)
##
##t.goto(0, 100)
##t.goto(100, 100)
##t.goto(100, 0)
##t.goto(0, 0)

##t.fd(150)
##t.goto(75, 50)
##t.home()

##a = 100
##
##t.penup()
##t.goto(-50, -50)
##
##t.pendown()
##t.goto(-50, 50)
##t.goto(50, 50)
##t.goto(50, -50)
##t.goto(-50, -50)

r = 36.18
t.penup()
t.goto(0, -r)

t.pendown()
t.circle(r)




# =================
turtle.done()
