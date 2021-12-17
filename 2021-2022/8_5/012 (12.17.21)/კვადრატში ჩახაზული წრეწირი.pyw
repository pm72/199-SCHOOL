import turtle

s = turtle.getscreen()
t = turtle.Turtle()


# ეკრანის კონგფიგურაცია
s.setup(1000, 600)
s.title("მართკუთხედი და წრეწირი ეკრანის სხვადსახვა მხარეს")
s.bgcolor('black')


# ხატვის სიჩქარე
t.speed(7)


# კვადრატი ცენტრში
t.pen(pensize=7, pencolor='salmon', fillcolor='DarkOliveGreen')

t.up()      # t.penup()
t.goto(-150, -150)

t.down()    # t.pendown()
t.begin_fill()
for side in range(4):
  t.fd(300)
  t.lt(90)
t.end_fill()


# წრეწირი ჩახაზული კვადრატში
t.pen(pensize=4, pencolor='Firebrick', fillcolor='Coral')

t.up()
t.fd(150)

t.down()
t.begin_fill()
t.circle(150)
t.end_fill()




# =======================
turtle.ht()
t.ht()

turtle.exitonclick()