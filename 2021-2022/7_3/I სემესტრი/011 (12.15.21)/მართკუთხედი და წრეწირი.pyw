import turtle

s = turtle.getscreen()
t = turtle.Turtle()

# ეკრანის კონფიგურაცია
s.setup(1000, 600)
s.title('მართკუთხედი და წრეწირი')
s.bgcolor('DarkOrchid')

t.speed(7)


# მართკუთხედი მარცხენა ზედა კუთხეში
t.pen(pensize=7, pencolor='salmon', fillcolor='OliveDrab')

t.up()       # t.penup()
t.goto(-400, 200)

t.down()     # t.pendown()
t.begin_fill()
for i in range(2):
  t.fd(250)
  t.rt(90)

  t.fd(150)
  t.rt(90)
t.end_fill()


# წრეწირი მარჯვენა ქვედა კუთხეში
t.pen(pensize=4, pencolor='DarkRed', fillcolor='LightCoral')

t.up()
t.goto(300, -200)

t.down()
t.begin_fill()
t.circle(100)
t.end_fill()




# ======================
turtle.exitonclick()