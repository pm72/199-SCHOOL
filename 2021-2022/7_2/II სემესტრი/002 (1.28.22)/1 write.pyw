import turtle

window = turtle.getscreen()
t = turtle.Turtle()

turtle.title("ტექსტი turtle ეკრანზე")
turtle.setup(1000, 600)

t.pen(pencolor='red')

# t.write("Hello, there!..", font=('calibri', 40, 'italic underline bold'))

t.up()
t.goto(0, 200)
t.down()

t.write("გამარჯობა, დღეს 28 იანვარია...",
        font=('calibri', 40, 'italic underline bold'),
        align='center')

# ===================
turtle.exitonclick()