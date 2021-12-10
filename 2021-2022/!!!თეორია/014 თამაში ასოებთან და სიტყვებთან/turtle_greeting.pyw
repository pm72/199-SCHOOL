import turtle

s = turtle.getscreen()
t = turtle.Turtle()

s.setup(960, 600)


name = turtle.textinput("", "What is your name? ")
greeting = f"Hi {name}!"

t.pencolor("darkviolet")

t.write(greeting, font=("Georgia", 45, "bold italic"),
align='center')




# ===============
turtle.ht()
t.ht()

turtle.exitonclick()
