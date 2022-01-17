import turtle

s = turtle.getscreen()
t = turtle.Turtle()

# ეკრანის კონფიგურცია
s.setup(800, 500)
s.bgcolor("DarkOrchid")
t.speed(8)

# სახატავი ფუნჯი
t.pensize(5)


# კვადრატი
t.up()
t.goto(-100, -100)

t.pen(pencolor='red', fillcolor='blue')

t.down()
t.begin_fill()
for i in range(4):
    t.fd(200)
    t.lt(90)
t.end_fill()


# წრე
t.up()
t.goto(0, -100)

t.pen(pencolor='magenta', fillcolor='cyan')

t.down()
t.begin_fill()
t.circle(100)
t.end_fill()




# =============
turtle.exitonclick()
