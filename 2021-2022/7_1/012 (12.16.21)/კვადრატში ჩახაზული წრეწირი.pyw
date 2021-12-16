import turtle

s = turtle.getscreen()
t = turtle.Turtle()

# ეკრანის კონფიგურაცია
s.setup(1000, 600)
s.title("მართკუთხედი და წრეწირი ეკრანის სხვადსხვა მხარეს")
s.bgcolor('DarkOrchid')


# ხატვის სიჩქარე
t.speed(7)


# კვადრატი ცენტრში
t.pen(pensize=7, pencolor='Teal', fillcolor='Peru')

t.up()      # t.penup()
t.goto(-150, -150)

t.down()
t.begin_fill()
for i in range(4):
  t.fd(300)
  t.lt(90)
t.end_fill()



# კვადრატში ჩახაზული წრეწირი
t.pen(pensize=4, pencolor='SlateGray', fillcolor='Linen')

t.up()
t.fd(150)

t.down()
t.begin_fill()
t.circle(150)
t.end_fill()






# ===================
t.ht()
turtle.ht()

turtle.exitonclick()