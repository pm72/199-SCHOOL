import turtle

s = turtle.getscreen()
t = turtle.Turtle()

# ეკრანის კონფიგურაცია
s.setup(1000, 600)
s.title("მართკუთხედი და წრეწირი ეკრანის სხვადასხვა მხარეს")
s.bgcolor('black')


# ხატვის სიჩქარე
t.speed(7)


# მართკუთხედი ცენტრში
t.pen(pensize=7, pencolor='Crimson', fillcolor='DarkKhaki')

t.up()
t.goto(-150, -150)

t.down()
t.begin_fill()
for side in range(4):
  t.fd(300)
  t.lt(90)
t.end_fill()


# წრეწირი ცენტრში
t.pen(pensize=5, pencolor='LightSlateGray', fillcolor='WhiteSmoke')

t.up()
t.fd(150)

t.down()
t.begin_fill()
t.circle(150)
t.end_fill()






# ======================
turtle.ht()
t.ht()

turtle.exitonclick()