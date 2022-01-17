import turtle

window = turtle.getscreen()
t = turtle.Turtle()

window.title("ფიგურების ხატვა")
window.setup(width=1000, height=600)

t.speed(8)

t.pen(pencolor='red', fillcolor='blue', pensize=2)

n = 5
t.begin_fill()
for i in range(n):
  t.fd(200)
  t.rt(144)
t.end_fill()




# ===============================
turtle.exitonclick()