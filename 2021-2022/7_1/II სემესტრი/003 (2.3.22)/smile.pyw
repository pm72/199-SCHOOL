import turtle


def move(x, y):
  t.pu()  # t.up()      t.pendown()
  t.goto(x, y)
  t.pd()  # t.down()    t.pendown()


window = turtle.getscreen()
t = turtle.Turtle()

turtle.title("Draw smile")
turtle.setup(500, 400)

t.pen(pensize=5, fillcolor='yellow', speed=10)
t.ht()
turtle.ht()

# თავი
move(0, -100)

t.begin_fill()
t.circle(100)
t.end_fill()

# თვალები
move(-40, 30)
t.dot(20)

move(40, 30)
t.dot(20)

# ცხვირი
move(0, 30)
t.goto(0, -35)

# ღიმილი
move(-35, -40)

t.setheading(-60)
t.circle(40, 120)

# ===============
turtle.exitonclick()