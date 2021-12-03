import turtle

s = turtle.getscreen()
t = turtle.Turtle()

t.speed(2)


'''
forward   => fd
backward  => bk,  back
right     => rt
left      => lt
'''

# Shida kutxeebis jami: (n - 2) * 180, n gverdebis raodenobaa.
# Shida kutxe: (n - 2) * 180 / n
# gare kutxe: 180 - (n - 2) * 180 / n


##n = 18
##a = 50
##angle = 180 - (n - 2) * 180 / n
##
##for i in range(n):
##  t.fd(a)
##  t.lt(angle)

##r = 100
##t.circle(r)

##w = 230
##h = 150
##
##t.goto(0, h)
##t.goto(w, h)
##t.goto(w, 0)
##t.goto(0, 0)

t.speed(1)

##w = 250
##h = 187
##
##t.penup()
##t.goto(-w/2, -h/2)
##
##t.pendown()
##t.goto(-w/2, h/2)
##t.goto(w/2, h/2)
##t.goto(w/2, -h/2)
##t.goto(-w/2, -h/2)

r = 100

t.dot(8)

t.penup()
t.goto(0, -r)

t.pendown()
t.circle(r)






# =================
turtle.ht()
t.ht()

turtle.done()
