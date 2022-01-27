import turtle

window = turtle.getscreen()
t = turtle.Turtle()

turtle.title("წარწერა turtle ეკრანზე")
turtle.setup(1000, 600)

t.pen(pencolor='red', pensize=5)

for i in range(5):
  t.setheading(0)
  t.fd(200)
  t.write(f"კუთხე გრადუსებში: {t.heading()}", font=('calibri', 12))

  t.up()
  t.home()
  t.down()

# ===============
turtle.exitonclick()