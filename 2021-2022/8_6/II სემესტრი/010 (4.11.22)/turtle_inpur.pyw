import turtle

s = turtle.getscreen()
t = turtle.Turtle()

turtle.title("Text input")
turtle.setup(1200, 400)

# name = input("What is your name? ")
name = turtle.textinput("Enter your name", "What is your name?")
number = int(turtle.numinput("", "Enter your favorite integer number"))
greeting = f"Welcome {name}!\n" \
           f"Your favorite number is {number}"

t.pencolor('darkviolet')

t.write(greeting, font=("Georgia", 45, 'bold italic'), align='center')


# ===================
turtle.ht()
t.ht()
turtle.exitonclick()