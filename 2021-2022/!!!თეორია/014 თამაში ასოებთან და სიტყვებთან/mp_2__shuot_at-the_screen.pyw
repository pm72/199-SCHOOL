import turtle

s = turtle.getscreen()
t = turtle.Turtle()

s.setup(960, 600)

message = turtle.textinput("", "Enter what's on your mind in 3 words or less: ")
shout = f"{message}!!!".upper()

t.pencolor('red')
t.write(shout, font=('arial black', 45, 'bold'), align='center')




# ===============
turtle.ht()
t.ht()

turtle.exitonclick()
