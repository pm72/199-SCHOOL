import turtle

window = turtle.getscreen()
t = turtle.Turtle()

window.title("ფიგურების ხატვა")
window.setup(1000, 600)
# # window.setup(width=1000, height=600, startx=0, starty=0)
# window.setup(starty=50, startx=50, width=1000, height=600)

n = 5
for i in range(n):
  t.fd(100)
  t.rt(144)




# ==================
turtle.exitonclick()