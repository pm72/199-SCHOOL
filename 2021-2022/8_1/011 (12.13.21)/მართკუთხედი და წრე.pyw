import turtle

s = turtle.getscreen()
t = turtle.Turtle()

# ეკრანის კონფიგურაცია
s.setup(1000, 600)
s.title('მართკუთხედი და წრეწირი სხვადასხვა მხარეს')
s.bgcolor('DarkOrchid')

t.speed(0)


# მართკუთხედი
t.up()    # t.penup()
t.goto(-400, 200)

t.pen(pensize=5, pencolor='salmon', fillcolor='Chartreuse')

t.down()   # t.pendown()

t.begin_fill()
for i in range(2):
    t.fd(250)
    t.rt(90)

    t.fd(150)
    t.rt(90)
t.end_fill()


# წრეწირი
t.up()
t.goto(300, -200)

t.pen(pensize=3, pencolor='Khaki', fillcolor='Navy')

t.down()

t.begin_fill()
t.circle(100)
t.end_fill()






# ==============
turtle.exitonclick()
