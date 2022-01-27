import turtle
from time import sleep

window = turtle.getscreen()
t = turtle.Turtle()

turtle.title("საკოორდინატო ღერძები")
turtle.setup(1000, 600)

t.pen(pencolor='blue', pensize=5)

# 0 კუთხე
t.setheading(0)
t.forward(200)
t.write(f"კუთხე გრადუსებში: {t.heading()}", font=('calibri', 12))

t.up()
t.home()
t.down()

# 90 კუთხე
t.setheading(90)
t.forward(200)
t.write(f"კუთხე გრადუსებში: {t.heading()}", font=('calibri', 12))

t.up()
t.home()
t.down()

# 180 კუთხე
t.setheading(180)
t.forward(200)
t.write(f"კუთხე გრადუსებში: {t.heading()}", font=('calibri', 12))

t.up()
t.home()
t.down()

# 270 კუთხე
t.setheading(270)
t.forward(200)
t.write(f"კუთხე გრადუსებში: {t.heading()}", font=('calibri', 12))

t.up()
t.home()
t.down()

# =================
turtle.exitonclick()