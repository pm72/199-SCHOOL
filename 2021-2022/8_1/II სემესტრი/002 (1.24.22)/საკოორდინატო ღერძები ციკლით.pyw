import turtle

window = turtle.getscreen()
t = turtle.Turtle()

window.title("საკოორდინატო ღერძები")
window.setup(1000, 600)

t.speed(0)

t.pen(pensize=3, pencolor='brown')

for i in range(0, 360, 90):   # range(start, stop, step)   [0, 360) ბიჯი 90
  t.setheading(i)
  t.fd(200)
  t.write(t.heading(), font=(12))

  t.up()
  t.home()
  t.down()




# ===================
# t.ht()
# turtle.ht()
turtle.exitonclick()