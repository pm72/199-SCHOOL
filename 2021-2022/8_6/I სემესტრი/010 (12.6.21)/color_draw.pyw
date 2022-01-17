import turtle

s = turtle.getscreen()
t = turtle.Turtle()
s.bgcolor('DarkOrchid')

# t.pencolor('salmon')
# t.fillcolor('Chartreuse')
# t.pensize(5)
# t.speed(5)
# t.color('salmon', 'chartreuse')
t.pen(pencolor='salmon', fillcolor='chartreuse',
speed=5, pensize=5)

t.begin_fill()
for i in range(4):
    t.fd(100)
    t.lt(90)
t.end_fill()




# ================
turtle.ht()
t.ht()

turtle.exitonclick()
