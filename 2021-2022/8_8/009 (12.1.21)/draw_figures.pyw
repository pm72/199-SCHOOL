import turtle

s = turtle.getscreen()
t = turtle.Turtle()

t.speed(1)

'''
forward    =>  fd
backward   =>  bk
right      =>  rt
left       =>  lt
'''

##t.fd(100)
##
##t.lt(39)
##t.fd(128)
##
##t.lt(82)
##t.fd(123)
##
##t.home()

##t.goto(200, 200)

##a = 100
##
##t.fd(a)
##
##t.lt(120)
##t.fd(a)
##
##t.home()

# SHIDA KUTXE: (n - 2) * 180 / n,  gverdebis raodenoba
# GARE KUTXE:  180 - (n - 2) * 180 / n

##n = 18
##a = 50
##angle = 180 - (n - 2) * 180 / n
##
##for i in range(n):
##  t.fd(a)
##  t.lt(angle)

##t.fd(100)
##
##t.lt(90)
##t.fd(100)
##
##t.lt(90)
##t.fd(100)
##
##t.home()

##a = 100
##
##t.goto(0, a)
##t.goto(a, a)
##t.goto(a, 0)
##t.goto(0, 0)

##a = 200
##
##t.penup()
##t.goto(-a/2, -a/2)
##
##t.pendown()
##t.dot(12)
##t.goto(-a/2, -a/2 + a)
##
##t.dot(12)
##t.goto(-a/2 + a, a/2)
##
##t.dot(12)
##t.goto(a/2, -a/2)
##
##t.dot(12)
##t.goto(-a/2, -a/2)
##
##t.penup()
##t.home()
##
##t.pendown()
##t.dot(10)

r = 200

t.penup()
t.goto(0, -r)

t.pendown()
t.circle(r)





# ----------------
turtle.hideturtle()
t.hideturtle()

turtle.done()
