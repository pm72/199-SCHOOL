import turtle

s = turtle.getscreen()
t = turtle.Turtle()

t.speed(3)

'''
forward   => fd
backward  => bk
right     => rt
lifrt     => lt
'''

# Shida kutxeebis jami: (n - 2) * 180
# Shida kutxe: (n - 2) * 180 / n
# Gare kutxe: 180 - (n - 2) * 180 / n


##n = 18
##a = 50
##angle = 180 - (n - 2) * 180 / n
##
##for i in range(n):
##  t.fd(a)
##  t.lt(angle)

##a = 200
##
##t.goto(0, a)
##t.goto(a, a)
##t.goto(a, 0)
##t.goto(0, 0)

##w = 236.38
##h = 116
##
##t.dot(8)
##
##t.penup()
##t.goto(-w/2, -h/2)
##
##t.pendown()
##t.dot(12)
##t.goto(-w/2, h/2)
##
##t.dot(12)
##t.goto(w/2, h/2)
##
##t.dot(12)
##t.goto(w/2, -h/2)
##
##t.dot(12)
##t.goto(-w/2, -h/2)

##r = 100
##t.color('red')
##t.circle(r)
##
##t.penup()
##t.color('green')
##t.goto(0, -r)
##
##t.pendown()
##t.circle(r)

##r = 80
##t.circle(r, 90)

n = 3
a = 150
angle = 180 - (n - 2) * 180 / n
r = 10

##t.fd(a)
##t.circle(r, angle)
##t.fd(a)
##t.circle(r, angle)

for i in range(n):
  t.fd(a)
  t.circle(r, angle)





# ==============
##turtle.hideturtle()
##t.hideturtle()

turtle.done()
