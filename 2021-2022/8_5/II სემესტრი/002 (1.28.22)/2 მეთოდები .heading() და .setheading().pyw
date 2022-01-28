import turtle

window = turtle.getscreen()
t = turtle.Turtle()

turtle.title("ტქსტი turtle ეკრანზე")
turtle.setup(1200, 600)

t.write(f"კუთხე: {t.heading()}", font=('calibri', 12))
t.fd(200)

# ====================
turtle.exitonclick()