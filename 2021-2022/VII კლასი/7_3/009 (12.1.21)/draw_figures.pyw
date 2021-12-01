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
##t.rt(90)
##t.fd(200)
##
##t.rt(90)
##t.fd(100)
##
##t.home()

##t.fd(150)
##
##t.lt(90)
##t.fd(100)
##
##t.home()

##a = 150
##
##t.fd(a+150)
##t.bk(150)
##
##t.lt(120)   # t.lt(180 - 60)
##t.fd(a)
##
##t.home()

#  mravalkutxedis shida kuutxebis jami
#  (n - 2) * 180, n - gverdebis raodenoba

##t.fd(100)
##
##t.rt(60)
##t.fd(100)
##
##t.rt(60)
##t.fd(100)
##
##t.rt(60)
##t.fd(100)
##
##t.rt(60)
##t.fd(100)
##
##t.home()

##t.goto(0, 100)
##t.goto(100, 100)
##t.goto(100, 0)
##t.goto(0, 0)

##a = 50
##
##t.penup()
##t.goto(-a, -a)
##
##t.pendown()
##t.goto(-a, a)
##t.goto(a, a)
##t.goto(a, -a)
##t.goto(-a, -a)


##a = 150
##b = 25
##
##t.fd(a)
##t.goto(a/2, b)
##t.home()

a = 50

t.penup()
t.goto(0, -a)

t.pendown()
t.circle(a)




# ================
turtle.hideturtle()
t.hideturtle()

turtle.done()
