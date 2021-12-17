import turtle

s = turtle.getscreen()
t = turtle.Turtle()


# ეკრანის კონფიგურაცია
s.setup(1000, 600)
s.title("კვადრატში ჩახაზული წრეწირი ეკრანის ცენტრში")
s.bgcolor('black')


# ხატვის სიჩქარე
t.speed(8)


# კვადრატი ეკრანის მარცხენა ზედა მხარეს
t.pen(pensize=7, pencolor='Teal', fillcolor='Peru')

t.up()      # t.penup()
t.goto(-150, -150)

t.down()    # t.pendown()
t.begin_fill()
for side in range(4):
  t.fd(300)
  t.lt(90)
t.end_fill()


# წრეწირი ეკრანის მარჯვენა ქვედა მხარეს
t.pen(pensize=5, pencolor='Maroon', fillcolor='Linen')

t.up()
t.goto(0, -150)

t.down()
t.begin_fill()
t.circle(150)
t.end_fill()




# ===================
# turtle.ht()
# t.ht()

turtle.exitonclick()