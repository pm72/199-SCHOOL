import turtle

window = turtle.getscreen()
t = turtle.Turtle()

window.title("ფიგურების ხატვა")
# window.setup(1000, 600)
# window.setup(width=1000, height=600, startx=0, starty=0)
# window.setup(startx=100, width=1000, starty=50)
window.setup(1000, 600)

n = 5    # (n - 2) * 180
for i in range(n):
  t.fd(100)
  t.lt(144)




# =======================
turtle.exitonclick()
# turtle.done()