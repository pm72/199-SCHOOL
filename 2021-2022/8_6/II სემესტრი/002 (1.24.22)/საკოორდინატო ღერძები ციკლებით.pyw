import turtle

window = turtle.getscreen()
t = turtle.Turtle()

window.title("საკოორდინატო ღერძები")
window.setup(width=1000, height=600)

t.speed(2)

t.pen(pensize=5, pencolor='red')

# 0 გრადუსი
for i in range(0, 360, 90):   # range(start, stop, step)
  t.setheading(i)
  t.fd(200)
  t.write(t.heading(), font=(12))

  t.up()
  t.home()
  t.down()




# =====================
# t.ht()
# turtle.ht()
turtle.exitonclick()