import turtle

s = turtle.getscreen()
t = turtle.Turtle()

# ეკრანის კონფიგურაცია
s.title("მართკუთხედი მარცხენა ზედა მხარეს და წრეწირი მარჯვენა ქვედა მხარეს")
s.setup(1000, 600)
s.bgcolor("black")

t.speed(7)


# მართკუთხედი ცენტრში
t.pen(pensize=7, pencolor='Teal', fillcolor='PaleGreen')

t.up()
t.goto(-150, -150)

t.down()
t.begin_fill()
for side in range(4):
  t.fd(300)
  t.lt(90)
t.end_fill()



# წრეწირი ცენტრში
t.pen(pensize=4, pencolor='LightSlateGray', fillcolor='Linen')

t.up()
t.fd(150)

t.down()
t.begin_fill()
t.circle(150)
t.end_fill()




# ====================
t.ht()
turtle.ht()

turtle.exitonclick()