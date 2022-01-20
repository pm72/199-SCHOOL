import turtle

s = turtle.getscreen()
t = turtle.Turtle()

# ეკრანის კონფიგურაცია
s.title("მართკუთხედი მარცხენა ზედა მხარეს და წრეწირი მარჯვენა ქვედა მხარეს")
s.setup(1000, 600)
s.bgcolor("DarkOrchid")

t.speed(7)


# მართკუთხედი მარცხენა ზედა მხარეს
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


# წრეწირი მარჯვენა ქვედა მხარეს
t.pen(pensize=4, pencolor='DarkRed', fillcolor='Coral')

t.up()
t.goto(300, -200)

t.down()
t.begin_fill()
t.circle(100)
t.end_fill()




# ====================
turtle.exitonclick()