import turtle

s = turtle.getscreen()
t = turtle.Turtle()

# ეკრანის კონფიგურაცია
s.title('ფერადი ხატვა')
s.bgcolor('black')
s.setup(1000, 600)

t.speed(8)


# კვადრატი
t.pen(pensize=5, pencolor='Maroon', fillcolor='Olive')

t.up()
t.goto(-100, -100)

t.down()
t.begin_fill()
for i in range(4):
  t.fd(200)
  t.lt(90)
t.end_fill()


# წრეწირი
t.pen(pensize=3, pencolor='white', fillcolor='white')

t.up()
t.fd(100)

t.down()
t.begin_fill()
t.circle(100)
t.end_fill()





# ====================
turtle.ht()
t.ht()

turtle.exitonclick()