import turtle

s = turtle.getscreen()
t = turtle.Turtle()

t.speed(8)

message = turtle.textinput('', 'ტექსტი')

t.up()
t.goto(0, 100)

t.down()
t.color('pink')
t.write(message, font=('Georgia', 45,
'bold italic underline'), align='center')




# ===============
turtle.ht()
t.ht()

turtle.exitonclick()
