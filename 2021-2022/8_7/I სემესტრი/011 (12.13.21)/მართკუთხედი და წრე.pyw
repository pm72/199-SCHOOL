import turtle

s = turtle.getscreen()
t = turtle.Turtle()

# ეკრანის კონფიგურაცია
s.setup(1000, 600)
s.bgcolor('DarkOrchid')
s.title('მართკუდხედი და წრე სხვადასხვა მხარეს')

t.speed(8)


# სახატავი ფუნჯი
t.pensize(10)


# მართკუთხედი
t.up()   # t.penup()
t.goto(-400, 250)

t.pen(pencolor='Salmon', fillcolor='Chartreuse')

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
t.goto(300, -200)

t.pen(pencolor='magenta', fillcolor='CornflowerBlue')

t.down()

t.begin_fill()
t.circle(100)
t.end_fill()






# ===============
turtle.exitonclick()
