import turtle

s = turtle.getscreen()
t = turtle.Turtle()


# ეკრანის კონფიგურაცია
s.setup(1000, 600)
s.title("მართკუთხედი და წრეწირი ეკრანის სხვადასხვა მხარეს")
s.bgcolor('DarkOrchid')


# ხატვის სიჩქარე
t.speed(8)


# მართკუთხედი ეკრანის მარცხენა ზედა მხარეს
t.pen(pensize=7, pencolor='salmon', fillcolor='DarkOliveGreen')

t.up()      # t.penup()
t.goto(-400, 200)

t.down()    # t.pendown()
t.begin_fill()
for side in range(2):
  t.fd(350)
  t.rt(90)

  t.fd(200)
  t.rt(90)
t.end_fill()


# წრეწირი ეკრანის მარჯვენა ქვედა მხარეს
t.pen(pensize=5, pencolor='Firebrick', fillcolor='Coral')

t.up()
t.goto(300, -200)

t.down()
t.begin_fill()
t.circle(100)
t.end_fill()




# ===================
turtle.ht()
t.ht()

turtle.exitonclick()