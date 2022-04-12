import turtle

s = turtle.getscreen()
t = turtle.Turtle()

turtle.title("Input in turtle screen")
turtle.setup(1200, 400)

text = turtle.textinput("", "Type any text")
# reversed_text = f"{text[::-1]}"    # Demetre
# message = f"Original text: {text}\nReversed text: {text[::-1]}"

t.pu()
t.goto(0, 100)
t.pd()
t.pencolor('darkviolet')
t.write(text, font=("Georgia", 45, 'bold italic'), align='center')

t.pu()
t.goto(0, 0)
t.pd()
t.pencolor('blue')
t.write(text[::-1], font=("Georgia", 45, 'bold italic'), align='center')





# =======================
turtle.ht()
t.ht()
turtle.exitonclick()