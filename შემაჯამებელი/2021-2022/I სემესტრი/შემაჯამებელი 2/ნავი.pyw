import turtle

s = turtle.getscreen()
t = turtle.Turtle()


# ეკრანის კონფიგურაცია
s.title("ნავი")
s.setup(800, 500)

t.speed(0)


# ცა
s.bgcolor("LightSkyBlue")


# წყალი
t.up()
t.goto(-400, -250)

t.down()
t.color("MediumBlue")

t.begin_fill()
for i in range(2):
    t.fd(800)
    t.lt(90)

    t.fd(100)
    t.lt(90)
t.end_fill()


# ნავი
t.pen(pencolor='SaddleBrown', fillcolor='SaddleBrown')

t.up()
t.goto(-150, -150)

t.down()

t.begin_fill()
t.fd(300)
t.goto(200, -75)
t.goto(-200, -75)
t.goto(-150, -150)
t.end_fill()


# აფრის დასამაგრებელი
t.pen(pencolor='black', fillcolor='black')
t.up()
t.goto(-5, -75)

t.down()
t.begin_fill()
for i in range(2):
    t.fd(10)
    t.lt(90)

    t.fd(200)
    t.lt(90)
t.end_fill()


# მარცხენა აფრა
t.pen(pencolor='white', fillcolor='white')

t.up()
t.goto(-5, 125)

t.down()
t.begin_fill()
t.goto(-190, -40)
t.goto(-5, -40)
t.end_fill()


# მარჯვენა აფრა
t.up()
t.goto(5, 125)

t.down()
t.begin_fill()
t.goto(190, -40)
t.goto(5, -40)
t.end_fill()


# მზე
t.pen(pencolor='yellow', fillcolor='yellow')

t.up()
t.goto(-320, 120)

t.down()
t.begin_fill()
t.circle(50)
t.end_fill()



# ===============
t.ht()
turtle.ht()

turtle.exitonclick()
