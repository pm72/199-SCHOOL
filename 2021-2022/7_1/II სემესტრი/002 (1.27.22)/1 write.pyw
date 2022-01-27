import turtle
from time import sleep

window = turtle.getscreen()
t = turtle.Turtle()

turtle.title("წარწერა გრაფიკულ ეკრანზე")
turtle.setup(1000, 600)

t.ht()
turtle.ht()

t.pen(pencolor='violet')

t.up()
t.goto(0, 200)
t.down()

# t.write("Hello, there!..", font=('calibri', 40, 'bold italic underline'))
t.write("გილოცავთ ნინოობას!",
        font=('calibri', 40, 'bold italic underline'),
        align='center')

highlight = 0.5
sleep(highlight)

for i in range(5):
  t.clear()
  sleep(highlight)
  t.write("გილოცავთ ნინოობას!",
          font=('calibri', 40, 'bold italic underline'),
          align='center')
  sleep(highlight)

# ==================
turtle.exitonclick()