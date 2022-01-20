import turtle

window = turtle.getscreen()
t = turtle.Turtle()

window.title('ფიგურები ხატვა')
# window.setup(1000, 600, 0, 0)
# window.setup(width=1000, height=600, startx=0, starty=0)
# window.setup(width=1000, startx=0)
# window.setup(1000, startx=50)
window.setup(1000, 600)

n = 5    # (n - 2) * 180
for i in range(n):
  t.fd(200)
  t.rt(144)




# =====================
turtle.exitonclick()