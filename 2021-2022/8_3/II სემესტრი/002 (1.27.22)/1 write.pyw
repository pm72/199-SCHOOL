import turtle
from time import sleep

window = turtle.getscreen()
t = turtle.Turtle()

turtle.title("წარწერა გრაფიკულ ეკრანზე")
turtle.setup(1000, 600)

t.pen(pencolor='brown')
t.ht()
turtle.ht()

t.up()
t.goto(0, 200)
t.down()

t.write("გილოცავთ ნინოობას!", font=('calibri', 40, 'bold underline italic'),
        align='center')
highlight = 0.2
sleep(highlight)

for i in range(7):
  t.clear()
  sleep(highlight)
  t.write("გილოცავთ ნინოობას!", font=('calibri', 40, 'bold underline italic'),
          align='center')
  sleep(highlight)


# =================
turtle.exitonclick()