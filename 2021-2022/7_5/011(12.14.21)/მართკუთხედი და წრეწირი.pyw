import turtle

s = turtle.getscreen()
t = turtle.Turtle()

# ეკრანის კონფიგურაცია
s.title('ფერადი ხატვა')
s.bgcolor('DarkOrchid')
s.setup(1000, 600)

t.speed(8)


# მართკუთხედი მარცხენა ზედა კუთხეში
t.pen(pensize=5, pencolor='Salmon', fillcolor='Crimson')

t.up()     # t.penup()
t.goto(-400, 200)

t.down()   # t.pendown()
t.begin_fill()
for i in range(2):
  t.fd(250)
  t.rt(90)

  t.fd(150)
  t.rt(90)
t.end_fill()


# წრეწირი მარჯვენა ქვედა კუთხეში
t.pen(pensize=3, pencolor='Teal', fillcolor='DarkGoldenrod')

t.up()
t.goto(300, -200)

t.down()
t.begin_fill()
t.circle(100)
t.end_fill()



# ====================
turtle.exitonclick()