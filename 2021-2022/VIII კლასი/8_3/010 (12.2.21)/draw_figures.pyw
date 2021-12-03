import turtle

s = turtle.getscreen()
t = turtle.Turtle()

t.speed(2)

'''
forward   => fd
backward  => bk
right     => rt
lifrt     => lt
'''

##t.goto(0, 100)
##t.goto(100, 100)
##t.goto(100, 0)
##t.goto(0, 0)

##w = 300
##h = 400
##
##t.penup()
##t.goto(-w/2, -h/2)
##
##t.pendown()
##t.goto(-w/2, h/2)
##t.goto(w/2, h/2)
##t.goto(w/2, -h/2)
##t.goto(-w/2, -h/2)

##r = 100
##
##t.dot()
##
##t.penup()
##t.goto(0, -r)
##
##t.pendown()
##t.circle(r)

##t.fd(150)
##t.goto(75, 200)
##t.goto(0, 0)
##
##t.fd(150)
##t.goto(75, -200)
##t.goto(0, 0)
##
##t.fd(-150)
##t.goto(-75, 200)
##t.goto(0, 0)
##
##t.fd(-150)
##t.goto(-75, -200)
##t.goto(0, 0)


# (n - 2) * 180

a = 100
n = 6
angle = 180 - (n - 2) * 180 / n

for i in range(n):
  t.fd(a)
  t.lt(angle)





# ==============
##turtle.hideturtle()
##t.hideturtle()

turtle.done()
