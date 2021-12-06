import turtle

# ენკარინის კონფიგურაცია
s = turtle.getscreen()
t = turtle.Turtle()
s.bgcolor('DarkOrchid')
s.title("ფერადი ხატვა")

# მოძრავი კუს კონფიგურაცია
t.pencolor('salmon')
t.fillcolor('Lime')
t.pensize(5)
t.speed(7)

t.begin_fill()
for i in range(4):
    t.fd(150)
    t.lt(90)
t.end_fill()





# ===============
turtle.ht()
t.ht()

turtle.exitonclick()
