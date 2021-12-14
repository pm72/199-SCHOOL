import turtle

s = turtle.getscreen()
t = turtle.Turtle()
t.pensize(10)
t.speed(0)


def set_position(x, y):
    t.penup()
    t.home()
    t.goto(x, y)
    t.pendown()


def letter_T():
    t.color('brown')

    t.fd(150)
    t.bk(75)
    t.rt(90)
    t.fd(150)


def letter_I():
    t.color('salmon')

    t.rt(90)
    t.fd(150)


def letter_M():
    t.color('red')

    t.rt(90)
    t.fd(150)
    t.bk(150)

    t.lt(30)
    t.fd(100)

    t.lt(120)
    t.fd(100)

    t.rt(150)
    t.fd(150)


def letter_O():
    t.color('green')

    t.circle(-75)



# ===================

set_position(-300, 100)
letter_T()

set_position(-100, 100)
letter_I()

set_position(-50, 100)
letter_M()

set_position(150, 100)
letter_O()


### oval
##t.shape('circle')
##t.shapesize(9, 3)   # (length, width, outline)



t.ht()
turtle.ht()
turtle.exitonclick()
