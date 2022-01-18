import turtle

window = turtle.getscreen()
t = turtle.Turtle()

window.title("ფიგურების ხატვა")
# window.setup(width=1000, height=600, startx=0, starty=0)
# window.setup(1000, 600, starty=0)
window.setup(1000, 600)

n = 5
for i in range(n):
  t.fd(100)
  t.rt(144)




# =============
turtle.exitonclick()