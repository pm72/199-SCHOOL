import turtle

window = turtle.getscreen()
t = turtle.Turtle()

window.title("ფიგურების ხატვა")
# window.setup(1000, 600)
# window.setup(1000, 600, 0, 0)
# window.setup(width=1000, height=600, startx=50, starty=0)
# window.setup(starty=100, width=1000, startx=50)
# window.setup(height=600, starty=100, width=1000, startx=50)
window.setup(1000, 600)

for i in range(4):
  t.fd(100)
  t.lt(90)




# ==================
# turtle.done()
turtle.exitonclick()