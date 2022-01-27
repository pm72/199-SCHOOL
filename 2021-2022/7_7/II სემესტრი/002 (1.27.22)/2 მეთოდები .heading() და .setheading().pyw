import turtle

window = turtle.getscreen()
t = turtle.Turtle()

turtle.title("წარწერა turtle ეკრანზე")
turtle.setup(1000, 600)

t.fd(200)
t.write(f"კუთხე გრადუსებში: {t.heading()}", font=('calibri', 12))

t.up()
t.home()
t.down()

t.setheading(-60)
t.fd(200)
t.write(f"კუთხე გრადუსებში: {t.heading()}", font=('calibri', 12))


# ===============
turtle.exitonclick()