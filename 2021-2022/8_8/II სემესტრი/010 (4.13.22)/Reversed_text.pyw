import turtle

s = turtle.getscreen()
t = turtle.Turtle()

turtle.title("Input in turtle window")
turtle.setup(width=1440, height=400)

text = turtle.textinput("", "Please,enter any text:")   # demetre

message = f"{text[::-1]}"

t.pencolor('gold')

t.write(message, font=("georgia", 30, 'bold italic'), align='center')


# ================
turtle.ht()
t.ht()
turtle.exitonclick()