import turtle

window = turtle.getscreen()
t = turtle.Turtle()

window.title("საკოორდინატო ღერძები")
window.setup(1000, 600)

t.pen(pensize=4, pencolor='brown', speed=0)

for i in range(0, 360, 90):    # range(start, stop, step)   start < stop
  t.setheading(i)
  t.fd(200)
  t.write(f"კუთხე: {t.heading()}", font=('calibri', 12))

  t.up()
  t.home()
  t.down()

# =======================
# t.ht()
# turtle.ht()
turtle.exitonclick()