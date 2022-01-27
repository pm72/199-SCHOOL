import turtle
from time import sleep

window = turtle.getscreen()
t = turtle.Turtle()

turtle.title("წარწერა გრაფიკულ ეკრანზე")
turtle.setup(1000, 600)

t.fd(200)
t.write(f"კუთხე გრადუსებში: {t.heading()}", font=('calibri', 12))

t.up()
t.home()
t.down()

t.setheading(360)
t.fd(200)
t.write(f"კუთხე გრადუსებში: {t.heading()}", font=('calibri', 12))

# ==================
turtle.exitonclick()