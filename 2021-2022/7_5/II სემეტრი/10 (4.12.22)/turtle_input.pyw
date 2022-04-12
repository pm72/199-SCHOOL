import turtle

s = turtle.getscreen()
t = turtle.Turtle()

turtle.title("Input in turtle window")
turtle.setup(1440, 400)

# name = input("What is your name? ")
name = turtle.textinput("Personal greeting info", "What is your name?")
age = int(turtle.numinput("Personal greeting info", "Please, enter your age"))

message = f"Welcome to here {name}!\n" \
          f"{name}, after 10 years you willl by {age + 10} yaers old."

t.pencolor("darkviolet")

t.write(message, font=("Georgia", 30, 'bold italic'), align='center')


# ===================
turtle.ht()
t.ht()
turtle.exitonclick()