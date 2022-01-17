import turtle

s = turtle.getscreen()
t = turtle.Turtle()

# ეკრანის კონფიგურცია
s.setup(800, 500)
s.bgcolor("DarkOrchid")
t.speed(5)

# სახატავი ფუნჯი
t.pensize(5)


# მართკუთხედი
t.up()   # t.penup()
t.goto(-350, 200)

t.pen(pencolor='Salmon', fillcolor='lime')

t.down()   # t.pendown()
t.begin_fill()
for i in range(2):
    t.fd(250)
    t.rt(90)

    t.fd(150)
    t.rt(90)
t.end_fill()


# წრე
t.up()
t.goto(250, -200)

t.pen(pencolor='Coral', fillcolor='SpringGreen')
t.down()

t.begin_fill()
t.circle(100)
t.end_fill()




# =============
turtle.exitonclick()
