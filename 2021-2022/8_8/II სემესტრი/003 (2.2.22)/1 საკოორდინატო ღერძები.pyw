import turtle

window = turtle.getscreen()
t = turtle.Turtle()

window.title("მეთოდები .heading() და .setheading()")
window.setup(1000, 600)

t.pen(pensize=4, pencolor='blue', speed=0)

for i in range(0, 360, 90):    # range(start=0, stop-1, step=1)    star < stop   start += step
  t.setheading(i)
  t.fd(200)
  t.write(f"კუთხე გრადუსებში: {t.heading()}", font=('calibri', 12))

  t.up()
  t.home()
  t.down()

# =========================
turtle.exitonclick()