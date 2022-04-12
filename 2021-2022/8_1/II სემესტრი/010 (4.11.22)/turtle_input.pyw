import turtle

s = turtle.getscreen()
t = turtle.Turtle()

turtle.title("Input text in turtle screen")
turtle.setup(1200, 400)

# name = input("What is your name? ")
name = turtle.textinput("", "What is your name?")
number = int(turtle.numinput("", "Enter your favorite integer number"))

message = f"Welcome to here {name}!\n" \
          f"{name}, your favorite number is {number}"

t.pencolor('darkviolet')

t.write(message, font=("Georgia", 35, 'bold italic'), align='center')


# =====================
turtle.ht()
t.ht()
turtle.exitonclick()