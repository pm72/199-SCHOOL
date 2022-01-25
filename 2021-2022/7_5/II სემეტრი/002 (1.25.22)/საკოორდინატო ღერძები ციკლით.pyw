import turtle

window = turtle.getscreen()
t = turtle.Turtle()

t.speed(8)

window.title("საკოორდინატო ღერძები")
window.setup(1000, 600)

t.pen(pensize=4, pencolor='red')

for i in range(0, 360, 15):   # range(start, stop, step)  [0; 360)  [0; 359]  ბიჯი 90
  t.setheading(i)
  t.fd(200)
  t.write(t.heading(), font=(12))

  t.up()
  t.home()
  t.down()




# ====================
turtle.exitonclick()