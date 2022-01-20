import turtle

window = turtle.getscreen()
t = turtle.Turtle()

window.title('წარწერა turtle ეკრანზე')

window.setup(1000, 600)

t.write("Hello, there!..", font=('Georgia', 40, 'italic underline'))




# ======================
turtle.exitonclick()