import turtle

s = turtle.getscreen()
t = turtle.Turtle()

# ეკრანის კონფიგურაცია
s.title("მართკუთხედი და წრეწირი ეკრანის სხვადასხვა მხარეს")
s.setup(1000, 600)
s.bgcolor('black')

t.speed(7)


# მართკუთხედი ცენტრში
t.pen(pensize=7, pencolor='salmon', fillcolor='DarkOliveGreen')

t.up()
t.goto(-150, -150)

t.down()
t.begin_fill()
for i in range(4):
  t.fd(300)
  t.lt(90)
t.end_fill()


# წრეწირი ცენტრში
t.pen(pensize=5, pencolor=('LightSlateGray'), fillcolor='Beige')

t.up()
t.fd(150)

t.down()
t.begin_fill()
t.circle(150)
t.end_fill()


# ==================
turtle.ht()
t.ht()

turtle.exitonclick()