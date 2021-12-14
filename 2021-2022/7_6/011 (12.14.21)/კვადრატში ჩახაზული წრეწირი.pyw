import turtle

s = turtle.getscreen()
t = turtle.Turtle()


# ეკრანის კონფიგურაცია
s.setup(1000, 600)
s.bgcolor('DarkOrchid')
s.title('კვადრატში ჩახაზული წრეწირი')

t.speed(8)


# კვადრატი ცენტრში
t.pen(pensize=5, pencolor='salmon', fillcolor='SeaGreen')

t.up()
t.goto(-150, -150)

t.down()
t.begin_fill()
for i in range(4):
  t.fd(300)
  t.lt(90)
t.end_fill()


# წრეწირი ცენტრში
t.pen(pensize=3, pencolor='DarkRed', fillcolor='Coral')

t.up()
t.fd(150)

t.down()
t.begin_fill()
t.circle(150)
t.end_fill()




# =================
turtle.exitonclick()