import turtle

s = turtle.getscreen()
t = turtle.Turtle()

turtle.title("Reverse name")
turtle.setup(1200, 400)

name = turtle.textinput("", "What is your name?")
reverse_name = name[::-1]

t.pencolor('darkviolet')

t.write(reverse_name, font=("Georgia", 45, 'bold italic'), align='center')


# ===================
turtle.ht()
t.ht()
turtle.exitonclick()