import turtle

s = turtle.getscreen()
t = turtle.Turtle()

turtle.title("Reversed text")
turtle.setup(1440, 400)

text = turtle.textinput("", "Please,enter any text:")    # demetre

message = f"Original text: {text}\n" \
          f"Reversed text: {text[::-1]}"

t.pencolor('gold')

t.write(message, font=("georgia", 30, 'bold italic'), align='center')


# ====================
turtle.ht()
t.ht()
turtle.exitonclick()