# მანდალა სწორი ხაზებით

import turtle

s = turtle.getscreen()
t = turtle.Turtle()

# ეკრანის კონფიგურაცია
s.setup(960, 500)
s.title("ფერადი ხატვა")
s.bgcolor("DarkOrchid")


# მოძრავი კუს კონფიგურაცია
t.speed(7)
t.pencolor('salmon')
t.fillcolor('Lime')
t.pensize(5)

t.begin_fill()
for i in range(2):
    t.fd(150)
    t.lt(90)

    t.fd(250)
    t.lt(90)
t.end_fill()


t.fillcolor('yellow')
t.begin_fill()
t.circle(100)
t.end_fill()





# =================
turtle.ht()
t.ht()

turtle.exitonclick()
