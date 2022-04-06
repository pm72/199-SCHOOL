import turtle

s = turtle.getscreen()
t = turtle.Turtle()

t.pen(pencolor='violet')

# name = input("What is your name? ")
name = turtle.textinput("Turtle text input", "What is your name?")
t.write(f"Welcome {name}!",
        font=('Georgia', 45, 'bold italic'),
        align='center')


# ================
turtle.ht()
t.ht()
turtle.exitonclick()