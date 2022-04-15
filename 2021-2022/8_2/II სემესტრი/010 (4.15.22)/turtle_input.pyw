# GUI  Graphic User Interface

import turtle

s = turtle.getscreen()
t = turtle.Turtle()

turtle.title("Input in turtle window")
turtle.setup(width=1440, height=400)

turtle.bgcolor('lightyellow')

# name = input("What is your name? ")
name = turtle.textinput("Personal info: Name", "What is your name?")
age = int(turtle.numinput("Personal info: Age", "Please, enter your age: "))
greeting = f"Welcome to here {name}!\n" \
           f"{name}, after 10 yars you will be {age + 10} years old."

t.pencolor('darkviolet')

t.write(greeting, font=("Georgia", 30, 'bold italic'), align='center')


# ==================
t.ht()
turtle.ht()
turtle.exitonclick()





# name = input("What is your name? ")
# age = int(input("Please, enter your age: "))
# greeting = f"Welcome to here {name}!\n" \
#            f"{name}, after 10 yars you will be {age + 10} years old."
#
# print(greeting)