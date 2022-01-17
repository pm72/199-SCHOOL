import turtle

s = turtle.getscreen()
t = turtle.Turtle()

# ეკრანის კონფიგურაცია
s.setup(1000, 600)
s.title('მართკუთხედი და წრეწირი სხვადასხვა მხარეს')
s.bgcolor('DarkOrchid')

t.speed(0)


# მართკუთხედი
t.up()
t.goto(-100, -100)

t.down()

t.pen(pensize=5, pencolor='magenta', fillcolor='CornflowerBlue')

t.begin_fill()
for i in range(4):
    t.fd(200)
    t.lt(90)
t.end_fill()


# წრეწირი
t.up()
t.goto(0, -80)

t.down()

t.pen(pensize=2, pencolor='Maroon', fillcolor='Goldenrod')

t.begin_fill()
t.circle(80)
t.end_fill()




# ==============
turtle.exitonclick()
