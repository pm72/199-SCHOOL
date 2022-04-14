import turtle

s = turtle.getscreen()
t = turtle.Turtle()

turtle.title("Input in turtle window")
turtle.setup(1440, 400)

# name = input("What is your name? ")
name = turtle.textinput("Personal info: Name", "What is your name?")
age = int(turtle.numinput("Personal info: Age", "Please, enter your age:"))

greeting = f"Welcome to here {name}!\n" \
           f"{name}, after 10 yers you will be {age + 10} yers old."

turtle.bgcolor("yellow")
t.pencolor('darkviolet')

t.write(greeting, font=("georgia", 30, 'bold italic'), align='center')


# ====================
turtle.ht()
t.ht()
turtle.exitonclick()