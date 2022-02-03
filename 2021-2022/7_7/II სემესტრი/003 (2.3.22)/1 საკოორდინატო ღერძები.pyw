import turtle

window = turtle.getscreen()
t = turtle.Turtle()

turtle.title("წარწერა turtle ეკრანზე")
turtle.setup(1000, 600)

t.pen(pencolor='red', pensize=5, speed=10)

for i in range(0, 360, 15):   # range(start, stop, step)  range(start=0, stop=360, step=90)  start < stop  start += step
  t.setheading(i)
  t.fd(200)
  t.write(f"კუთხე გრადუსებში: {t.heading()}", font=('calibri', 12))

  t.up()
  t.home()
  t.down()

# ===============
turtle.exitonclick()

# range(5)   [0,1,2,3,4]  range(start=0, stop=5, step=1)
# range(2, 5)   [2,3,4]  range(start=2, stop=5, step=1)
# range(7, 18, 3)   [7,10,13, 16]  range(start=7, stop=18, step=3)