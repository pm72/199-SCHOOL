# GUI   Grafic User Interface

import turtle, math

s = turtle.getscreen()
t = turtle.Turtle()

turtle.title("Input in turtle window")
turtle.setup(1440, 400)

turtle.bgcolor('lightyellow')

# name = input("What is your name? ")
name = turtle.textinput("Personal info: Name", "What is your name?")
age = math.ceil(turtle.numinput("Personal info: Age", "Please, enter your age:"))

greeting = f"Welcome to here {name}!\n" \
           f"{name}, after 10 yers you will be {age + 10} years old."

t.pencolor('darkviolet')

t.write(greeting, font=("georgia", 30, 'bold italic'), align='center')


# ================
t.ht()
turtle.ht()
turtle.exitonclick()