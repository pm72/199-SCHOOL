import turtle

s = turtle.getscreen()
t = turtle.Turtle()

# ეკრანის კონფიგურაცია
s.setup(1000, 600)
s.bgcolor('DimGray')
s.title('კვადრატში ჩახაზული წრეწირი')

t.speed(8)


# კვადრატი
t.pen(pensize=7, pencolor='RosyBrown', fillcolor='BlanchedAlmond')

t.up()
t.goto(-150, -150)

t.down()
t.begin_fill()
for i in range(4):
  t.fd(300)
  t.lt(90)
t.end_fill()


# წრეწირი
t.pen(pensize=3, pencolor='Navy', fillcolor='LightSteelBlue')

t.up()
t.fd(150)

t.down()
t.begin_fill()
t.circle(150)
t.end_fill()





# ===================
turtle.exitonclick()