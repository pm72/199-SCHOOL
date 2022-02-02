import turtle


def move(x, y):
  t.pu()  # t.penup()     t.up()
  t.goto(x, y)
  t.pd()  # t.pendown()   t.down()


window = turtle.getscreen()
t = turtle.Turtle()

turtle.title("Draw smile")
turtle.setup(800, 500)

t.pen(pensize=5, fillcolor='yellow', speed=12)
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
move(-35, -35)

t.setheading(-60)
t.circle(40, 120)

# ====================
turtle.exitonclick()