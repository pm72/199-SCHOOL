import turtle
from time import sleep

window = turtle.getscreen()
t = turtle.Turtle()

turtle.title("2 მეთოდები .heading() და .setheading()")
turtle.setup(1000, 600)

t.forward(200)
t.write(f"კუთხე გრადუსებში: {t.heading()}", font=('calibri', 12))

t.up()
t.home()
t.down()

t.setheading(60)
t.forward(200)
t.write(f"კუთხე გრადუსებში: {t.heading()}", font=('calibri', 12))

# =================
turtle.exitonclick()