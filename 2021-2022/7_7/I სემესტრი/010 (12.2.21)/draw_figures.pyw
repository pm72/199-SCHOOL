import turtle

s = turtle.getscreen()
t =turtle.Turtle()

'''
forward   => fd
backward  => bk
right     => rt
left      => lt
'''

t.speed(2)

##a = 150
##
##t.goto(0, a)
##t.goto(a, a)
##t.goto(a, 0)
##t.goto(0, 0)

##w = 200
##h = 300
##
##t.penup()
##t.goto(-w/2, -h/2)
##
##t.pendown()
##t.dot(10)
##
##t.goto(-w/2, h/2)
##t.dot(10)
##
##t.goto(w/2, h/2)
##t.dot(10)
##
##t.goto(w/2, -h/2)
##t.dot(10)
##
##t.goto(-w/2, -h/2)
##
##t.penup()
##t.home()
##
##t.pendown()
##t.dot()


##r = 100
##
##t.dot()
##
##t.penup()
##t.goto(0, -r)
##
##t.pendown()
##t.circle(r)

a = 150


for i in range(3):
  t.fd(a)
  t.circle(20, 120)




# =================
turtle.hideturtle()
t.hideturtle()

turtle.done()
