import turtle

window = turtle.getscreen()
t = turtle.Turtle()

window.title('ფიგურების ხატვა')
# window.setup(1000, 600, startx=50, starty=50)
window.setup(1000, 600)

n = 5
for i in range(n):
  t.fd(200)
  t.rt(144)

# ======================
turtle.exitonclick()