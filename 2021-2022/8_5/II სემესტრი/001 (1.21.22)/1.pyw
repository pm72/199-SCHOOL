import turtle

window = turtle.getscreen()
t = turtle.Turtle()

window.title("ფიგურების ხატვა")
# window.setup(1000, 600, 0, 0)
# window.setup(width=1000, height=600, startx=0, starty=0)
# window.setup(height=500, width=1000, startx=50)
window.setup(1000, 600)

n = 6    # (n - 2) * 180
for i in range(n):
  t.fd(100)
  t.lt(360 / n)




# =====================
# turtle.done()
turtle.exitonclick()