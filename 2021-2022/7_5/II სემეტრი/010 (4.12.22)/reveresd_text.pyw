import turtle

s = turtle.getscreen()
t = turtle.Turtle()

turtle.title("Reversed text")
turtle.setup(1440, 400)

text = turtle.textinput("", "Please, enter any text")   # demetre

t.pencolor("gold")

message = f"Original text: {text}\n" \
          f"Reversed text: {text[::-1]}"

t.write(message, font=("Georgia", 30, 'bold italic'), align='center')


# ===================
turtle.ht()
t.ht()
turtle.exitonclick()