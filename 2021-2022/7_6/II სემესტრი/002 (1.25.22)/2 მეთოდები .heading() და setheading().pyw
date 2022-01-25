import turtle

window = turtle.getscreen()
t = turtle.Turtle()

window.title("2 მეთოდები .heading() და setheading()")
window.setup(1000, 600)

# t.write(f"გრადუსი: {t.heading()}", font=('calibri', 12))
t.fd(200)

t.up()
t.home()
t.down()

t.setheading(-60)
t.write(f"გრადუსი: {t.heading()}", font=('calibri', 12))
t.fd(200)




# ==================
turtle.exitonclick()