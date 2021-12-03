import turtle

s = turtle.getscreen()
t = turtle.Turtle()

t.speed(2)


'''
forward      => fd
backward     => bk,  back
right        => rt
left         => lt
hideturtle   => ht
'''

# shida kutxeebis jami: (n - 2)  * 180, n gverdebis raodenoba
# shida kutxe: (n - 2)  * 180 / n
# gare kutxe: 180 - (n - 2)  * 180 / n


##a = 100
##n = 8
##angle = 180 - (n - 2)  * 180 / n
##
##for i in range(n):
##  t.fd(a)
##  t.lt(angle)

##t.dot(8)
##t.goto(200, 200)
##t.dot(8)

##w = 250
##h = 150
##
##t.goto(0, h)
##t.goto(w, h)
##t.goto(w, 0)
##t.goto(0, 0)


w, h = 250, 250


t.dot(8)

t.penup()
t.goto(-w/2, -h/2)

t.pendown()
t.dot(12)
t.goto(-w/2, -h/2 + h)

t.dot(12)
t.goto(-w/2 + w, h/2)

t.dot(12)
t.goto(w/2, -h/2)

t.dot(12)
t.goto(-w/2, -h/2)




# =================
turtle.ht()
t.ht()

turtle.done()
