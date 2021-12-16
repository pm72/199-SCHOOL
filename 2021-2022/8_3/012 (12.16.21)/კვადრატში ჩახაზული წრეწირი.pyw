import turtle

s = turtle.getscreen()
t = turtle.Turtle()

# ეკრანის კონფიგურაცია
s.title('მართკუთხედი მარცხენა ზედა მხარე და წრეწირი მარჯვენა ქვედა მხარეს')
s.bgcolor('black')
s.setup(1000, 600)

# ხატვის სიჩქარე
t.speed(7)


# კვადრატი ცენტრში
t.pen(pensize=7, pencolor='SlateGray', fillcolor='Coral')

t.up()
t.goto(-150, -150)

t.down()
t.begin_fill()
for side in range(4):
  t.fd(300)
  t.lt(90)
t.end_fill()



# კვადრატში ჩახაზული წრეწირი
t.pen(pensize=4, pencolor='MediumVioletRed', fillcolor='Linen')

t.up()
t.fd(150)

t.down()
t.begin_fill()
t.circle(150)
t.end_fill()







# =====================
turtle.ht()
t.ht()

turtle.exitonclick()