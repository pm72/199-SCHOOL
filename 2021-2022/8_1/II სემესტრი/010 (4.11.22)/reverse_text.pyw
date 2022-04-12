import turtle

s = turtle.getscreen()
t = turtle.Turtle()

turtle.title("Input text in turtle screen")
turtle.setup(1200, 400)

text = turtle.textinput("", "What is your name?")
# reversed_text = f"{text[::-1]}"   # Demetre
message = f"Originat text: {text}\n" \
          f"Reversed text: {text[::-1]}"

t.pencolor('darkviolet')
t.write(message, font=("Georgia", 35, 'bold italic'), align='center')

# =====================
turtle.ht()
t.ht()
turtle.exitonclick()