import turtle

s = turtle.getscreen()
t = turtle.Turtle()

turtle.title("Input in turtle window")
turtle.setup(width=1440, height=400)

# name = input("What is your name? ")
name = turtle.textinput("Personal info: Name", "What is your name?")
age = int(turtle.numinput("Personal info: Age", "Please, enter your age:"))

message = f"Welcome to here {name}!\n" \
          f"{name}, after 10 years you will bi {age + 10} years old."

turtle.bgcolor('lightyellow')
t.pencolor('darkviolet')

t.write(message, font=("georgia", 30, 'bold italic'), align='center')


# ================
turtle.ht()
t.ht()
turtle.exitonclick()