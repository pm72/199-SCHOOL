import turtle

window = turtle.getscreen()
t = turtle.Turtle()

window.title('ფიგურების ხატვა')
# window.setup(1000, 600, 0, 0)
# window.setup(width=1000, height=600, startx=0, starty=0)
# window.setup(startx=50, width=890, starty=150, height=150)
window.setup(1000, 600)

n = 5    # (n - 2) * 180
for i in range(n):
  t.fd(200)
  t.rt(144)




# ======================
turtle.exitonclick()